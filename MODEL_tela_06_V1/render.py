import functools,json,threading,argparse,hashlib
from pathlib import Path
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
assert (ROOT/'index.html').exists(),'Expected implemented index.html; HTML absent (TDD red)'
p=argparse.ArgumentParser();p.add_argument('--candidate',action='store_true');args=p.parse_args()
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT.parent)));threading.Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/{ROOT.name}/';report={'DPR':1,'viewports':[],'version':(ROOT/'VERSION').read_text().strip()}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);report['browser']=browser.version
 for w,h in ([(390,844)] if args.candidate else [(375,812),(390,844),(430,932)]):
  context=browser.new_context(viewport={'width':w,'height':h},device_scale_factor=1);page=context.new_page();errors=[];network=[];external=[]
  def route(r):
   if r.request.url.startswith('http://127.0.0.1:') or r.request.url.startswith('data:'):r.continue_()
   else:external.append(r.request.url);r.abort()
  context.route('**/*',route)
  page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None);page.on('response',lambda r:network.append(r.url) if r.status>=400 else None);page.on('requestfailed',lambda r:network.append(r.url))
  page.goto(url,wait_until='networkidle');page.evaluate('document.fonts.ready');page.screenshot(path=str(ROOT/(f'candidato-{w}.png' if args.candidate else f'screenshots/{w}x{h}.png')))
  state=page.evaluate('''()=>({viewport:[innerWidth,innerHeight],document:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],conversation:[conversation.scrollHeight,conversation.clientHeight],images:[...document.querySelectorAll('.photo')].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0,fit:getComputedStyle(i).objectFit,natural:[i.naturalWidth,i.naturalHeight],render:[i.getBoundingClientRect().width,i.getBoundingClientRect().height]})),targets:[...document.querySelectorAll('button,a,input')].filter(e=>e.getClientRects().length).map(e=>({name:e.id,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}))})''')
  assert state['conversation'][0]<=state['conversation'][1],state['conversation'];assert state['document']==[w,h];assert all(i['loaded'] for i in state['images']);assert all(t['width']>=44 and t['height']>=44 for t in state['targets']),state['targets']
  for id in ['phone','options','details','office','attachment']:
   b=page.locator('#'+id);b.focus();page.keyboard.press('Enter');assert page.locator('#panel').is_visible();page.keyboard.press('Tab');assert page.evaluate("document.activeElement.id==='close'");page.keyboard.press('Escape');page.wait_for_function('(id)=>document.activeElement.id===id',arg=id)
  inp=page.locator('#message');inp.fill('   ');inp.press('Enter');assert page.locator('.new-message').count()==0
  inp.fill('Mensagem local de teste');inp.press('Enter');assert page.locator('.new-message').count()==1;assert inp.evaluate('e=>e===document.activeElement')
  literal='<img src=x onerror=alert(1)>';inp.fill(literal);page.locator('#send').click();assert page.locator('.new-message').last.inner_text()==literal;assert page.locator('.new-message img').count()==0
  inp.fill('Mensagem longa '*100);inp.press('Enter');assert page.locator('.new-message').count()==3;assert page.evaluate('conversation.scrollHeight>conversation.clientHeight');assert page.evaluate('document.documentElement.scrollWidth===innerWidth')
  page.reload(wait_until='networkidle');assert page.locator('.new-message').count()==0
  page.locator('#back').click();page.wait_for_load_state();assert 'MODEL_tela_05_V1' in page.url
  state.update(errors=errors,networkErrors=network,externalRequests=external,actions='Five panels via keyboard; focus trapped/restored; Escape; empty/common/literal/long sends; memory reset; real back05 passed');assert not errors and not network and not external
  report['viewports'].append(state);context.close()
 if not args.candidate:
  context=browser.new_context(viewport={'width':375,'height':812},device_scale_factor=1,reduced_motion='reduce');context.route('**/*.png',lambda r:r.abort());page=context.new_page();page.goto(url,wait_until='networkidle');assert page.locator('.photo.failed').count()==4;assert page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches");page.locator('#message').fill('Fallback');page.locator('#message').press('Enter');assert page.locator('.new-message').count()==1;page.locator('#phone').click();page.keyboard.press('Escape');report['fallback']={'separateContext':True,'reducedMotion':True,'failedPhotos':4,'composerAndPanel':True};context.close()
 browser.close()
server.shutdown();report['sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and p.suffix in ['.html','.css','.js','.png']};(ROOT/('relatorio-candidato.json' if args.candidate else 'relatorio-browser.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))
