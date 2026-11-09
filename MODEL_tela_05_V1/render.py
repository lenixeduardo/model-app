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
report={'DPR':1,'viewports':[]}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);report['browser']=browser.version
 for w,h in ([(390,844)] if args.candidate else [(375,812),(390,844),(430,932)]):
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1);errors=[];network=[]
  page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None);page.on('response',lambda r:network.append(r.url) if r.status>=400 else None);page.on('requestfailed',lambda r:network.append(r.url))
  page.goto(f'http://127.0.0.1:{server.server_port}/{ROOT.name}/',wait_until='networkidle');page.screenshot(path=str(ROOT/(f'candidato-{w}.png' if args.candidate else f'captura-{w}.png')))
  state=page.evaluate('''()=>({viewport:[innerWidth,innerHeight],document:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],images:[...document.querySelectorAll('.tile img')].map(i=>({src:i.src,loaded:i.complete&&i.naturalWidth>0,fit:getComputedStyle(i).objectFit,natural:[i.naturalWidth,i.naturalHeight]})),targets:[...document.querySelectorAll('button,a')].filter(e=>e.getClientRects().length).map(e=>({name:e.ariaLabel||e.textContent,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}))})''')
  assert state['document']==[w,h];assert all(i['loaded'] and i['fit']=='cover' for i in state['images']);assert all(t['width']>=44 and t['height']>=44 for t in state['targets'])
  for tab in ['videos','trabalhos','fotos']:
   page.locator('#'+tab).click();assert page.locator('#'+tab).get_attribute('aria-selected')=='true'
  for i in range(1,8):
   e=page.locator(f'[data-photo="{i}"]');e.click();assert page.locator('#viewer').is_visible();page.keyboard.press('Escape');assert e.evaluate('e=>e===document.activeElement')
  page.locator('#search').click();page.locator('#query').fill('zzzz');assert page.locator('#results').inner_text()=='Nenhum recorte encontrado.';page.locator('#query').fill('camisa');assert page.locator('#results button').count()>0;page.keyboard.press('Escape');page.wait_for_function("document.activeElement.id==='search'")
  page.locator('#back').click();page.wait_for_load_state();assert 'MODEL_tela_04_V1' in page.url
  state.update(errors=errors,networkErrors=network,actions='Tabs, seven crop dialogs, Escape, focus restoration, local search and real back04 passed');assert not errors and not network
  report['viewports'].append(state);page.close()
 browser.close()
server.shutdown();report['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.glob('*') if p.suffix in ['.html','.css','.js','.png']};(ROOT/('relatorio-candidato.json' if args.candidate else 'relatorio-browser.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))
