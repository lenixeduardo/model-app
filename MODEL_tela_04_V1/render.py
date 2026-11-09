import functools,json,threading,argparse
from pathlib import Path
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
assert (ROOT/'index.html').exists(),'Expected implemented index.html; HTML absent (TDD red)'
parser=argparse.ArgumentParser();parser.add_argument('--candidate',action='store_true');args=parser.parse_args()
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*a): pass
server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT.parent)));threading.Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/{ROOT.name}/'
report={'DPR':1,'viewports':[]}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for w,h in ([(390,844)] if args.candidate else [(375,812),(390,844),(430,932)]):
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1);errors=[];network=[]
  page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None);page.on('response',lambda r:network.append(r.url) if r.status>=400 else None);page.on('requestfailed',lambda r:network.append(r.url))
  assert page.goto(url,wait_until='networkidle').status==200
  page.screenshot(path=str(ROOT/(f'candidato-{w}.png' if args.candidate else f'captura-{w}.png')))
  state=page.evaluate('''()=>({size:[innerWidth,innerHeight],document:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],images:[...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0,fit:getComputedStyle(i).objectFit})),targets:[...document.querySelectorAll('button,a')].filter(e=>e.getClientRects().length).map(e=>({label:e.ariaLabel||e.textContent.trim(),width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})),reducedMotion:!![...document.styleSheets].flatMap(s=>[...s.cssRules]).find(r=>r.conditionText?.includes('prefers-reduced-motion'))})''')
  assert state['document']==[w,h],state
  assert all(i['loaded'] for i in state['images']);assert all(t['width']>=44 and t['height']>=44 for t in state['targets']),state['targets']
  page.locator('#save').click();assert page.locator('#save').get_attribute('aria-pressed')=='true'
  for selector in ['#contact','#share','#options','#send']+[f'[data-photo="{i}"]' for i in range(1,5)]:
   page.locator(selector).click();assert page.locator('dialog').is_visible();page.keyboard.press('Escape');assert not page.locator('dialog').is_visible();assert page.locator(selector).evaluate('e=>e===document.activeElement')
  page.locator('#contact').focus();assert page.locator('#contact').evaluate('e=>getComputedStyle(e).outlineStyle')!='none'
  page.locator('#back').click();page.wait_for_load_state();assert 'MODEL_tela_03_V2' in page.url;assert page.title()=='Enzo, 26 — MODEL'
  state.update(errors=errors,networkErrors=network,actions='save, 4 photo crops, contact/share/options/send dialogs, Escape, return focus and real back passed');assert not errors and not network
  report['viewports'].append(state);page.close()
 browser.close()
server.shutdown();(ROOT/('relatorio-candidato.json' if args.candidate else 'relatorio-browser.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))
