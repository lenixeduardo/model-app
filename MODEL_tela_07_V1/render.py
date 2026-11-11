import functools,json,threading,argparse,hashlib
from pathlib import Path
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
assert (ROOT/'index.html').exists(),'HTML absent: TDD red'
a=argparse.ArgumentParser();a.add_argument('--candidate',action='store_true');args=a.parse_args()
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT.parent)));threading.Thread(target=server.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{server.server_port}/{ROOT.name}/'
report={'DPR':1,'version':(ROOT/'VERSION').read_text().strip(),'viewports':[]}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);report['browser']=browser.version
 for w,h in ([(390,844)] if args.candidate else [(375,812),(390,844),(430,932)]):
  c=browser.new_context(viewport={'width':w,'height':h},device_scale_factor=1);page=c.new_page();errors=[];network=[];external=[]
  page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None);page.on('response',lambda r:network.append(r.url) if r.status>=400 else None)
  def route(r):
   if r.request.url.startswith('http://127.0.0.1:') or r.request.url.startswith('data:'):r.continue_()
   else:external.append(r.request.url);r.abort()
  c.route('**/*',route);page.goto(url,wait_until='networkidle');assert page.locator('.casting').count()==3
  page.screenshot(path=str(ROOT/(f'candidato-{w}.png' if args.candidate else f'captura-{w}.png')))
  state=page.evaluate('''()=>({viewport:[innerWidth,innerHeight],document:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],images:[...document.querySelectorAll('.photo')].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0,natural:[i.naturalWidth,i.naturalHeight],render:[i.width,i.height],fit:getComputedStyle(i).objectFit})),targets:[...document.querySelectorAll('button,a')].filter(e=>e.getClientRects().length).map(e=>({name:e.getAttribute('aria-label')||e.textContent,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}))})''');assert state['document']==[w,h];assert all(i['loaded'] for i in state['images']);
  for image in state['images']:
   nw,nh=image['natural'];rw,rh=image['render'];scale=max(rw/nw,rh/nh) if image['fit']=='cover' else min(rw/nw,rh/nh);visible=min(1,rw/(nw*scale))*min(1,rh/(nh*scale));image['visibleSourceFraction']=visible;image['ratioError']=abs(rw/rh-nw/nh);assert visible>0.995 and image['ratioError']<0.015,('Source framing clipped or stretched',image)
  assert all(t['width']>=44 and t['height']>=44 for t in state['targets']),state
  for name,count in [('Moda',1),('Comercial',1),('Editorial',2),('Todos',3)]:
   page.get_by_role('button',name=name,exact=True).click();assert page.locator('.casting').count()==count
  saves=page.locator('.save');saves.nth(0).click();assert saves.nth(0).get_attribute('aria-pressed')=='true';assert saves.nth(1).get_attribute('aria-pressed')=='false';assert not page.locator('dialog').is_visible();saves.nth(0).click();assert saves.nth(0).get_attribute('aria-pressed')=='false';saves.nth(0).click();page.reload(wait_until='networkidle');assert page.locator('.save[aria-pressed=true]').count()==0
  for locator in [page.locator('.open-card').first]+[page.locator('#'+s) for s in ['create','add','search','profile']]:
   locator.focus();page.keyboard.press('Enter');assert page.locator('dialog').is_visible();assert page.evaluate("document.activeElement.id==='close'");page.keyboard.press('Tab');assert page.evaluate("document.activeElement.id==='close'");page.keyboard.press('Escape');page.wait_for_function('(e)=>e===document.activeElement',arg=locator.element_handle())
  page.get_by_role('link',name='Chat',exact=True).click();page.wait_for_load_state();assert 'MODEL_tela_06_V1' in page.url;page.goto(url);page.get_by_role('link',name='Descobrir',exact=True).click();page.wait_for_load_state();assert 'MODEL_tela_03_V2' in page.url
  state.update(console=errors,networkErrors=network,externalRequests=external,actions='Filters 3/1/1/2; isolated save toggles; reload reset; five keyboard dialogs with trapped and restored focus/Escape; real links03/06 passed');assert not errors and not network and not external;report['viewports'].append(state);c.close()
 if not args.candidate:
  c=browser.new_context(viewport={'width':390,'height':844},reduced_motion='reduce');c.route('**/*.png',lambda r:r.abort());page=c.new_page();page.goto(url,wait_until='networkidle');assert page.locator('.photo.failed').count()==3;assert page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches");page.locator('#create').click();page.keyboard.press('Escape');report['fallback']={'separateContext':True,'failedPhotos':3,'reducedMotion':True,'dialogOperational':True};c.close()
 browser.close()
server.shutdown();
if not args.candidate:
 import runpy
 runpy.run_path(str(ROOT/'compare.py'))
report['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir() if p.suffix in ['.html','.css','.js','.png']};(ROOT/('relatorio-candidato.json' if args.candidate else 'relatorio-browser.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))
