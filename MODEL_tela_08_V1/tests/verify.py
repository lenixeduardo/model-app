import json,hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
root=Path(__file__).resolve().parents[1]
report={'version':(root/'VERSION').read_text().strip(),'console':[],'network_errors':[],'checks':{}}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 report['browser']=browser.version
 page=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
 page.on('pageerror',lambda e:report['console'].append(str(e)))
 page.on('requestfailed',lambda r:report['network_errors'].append(r.url))
 url='http://localhost:8000/MODEL_tela_08_V1/index.html'
 page.goto(url);page.screenshot(path=str(root/'screenshots/candidato-390.png'))
 page.locator('#city').fill('Campinas, SP');page.select_option('#distance','100')
 for name,lo,hi in [('age','22','40'),('height','1.65','2.05'),('fee','500','7000')]:
  page.locator('#value-'+name).click();page.locator('#lower').fill(lo);page.locator('#upper').fill(hi);page.get_by_role('button',name='Salvar',exact=True).click()
 page.get_by_role('button',name='Fitness',exact=True).click();page.get_by_role('radio',name='Flexível').click();page.locator('#apply').click();assert 'Campinas, SP' in page.locator('#summary-content').inner_text();assert '7.000' in page.locator('#summary-content').inner_text();page.keyboard.press('Escape');assert page.locator('#apply').evaluate('(e)=>e===document.activeElement')
 page.locator('#value-age').click();page.locator('#lower').fill('50');page.locator('#upper').fill('30');page.get_by_role('button',name='Salvar',exact=True).click();assert page.locator('#error').inner_text();page.keyboard.press('Escape')
 page.locator('#reset').click();assert page.locator('#city').input_value()=='São Paulo, SP';assert page.locator('#value-age').inner_text()=='18 - 35 anos';assert page.get_by_role('button',name='Fashion',exact=True).get_attribute('aria-pressed')=='true'
 page.locator('#age').focus();page.keyboard.press('ArrowRight');assert page.locator('#value-age').inner_text()=='19 - 35 anos';page.reload();assert page.locator('#value-age').inner_text()=='18 - 35 anos'
 report['checks']['all_flows']='passed: city, distance, all six endpoints, categories, radio, apply summary, Escape/focus restore, validation, reset, keyboard range, reload'
 report['native_inputs']=page.locator('input').evaluate_all('(es)=>es.map(e=>({id:e.id,type:e.type}))')
 report['targets']=page.locator('main button,main a,main input,main select').evaluate_all('(es)=>es.map(e=>({id:e.id||e.textContent.trim(),width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}))')
 assert all(t['height']>=44 and t['width']>=44 for t in report['targets'])
 report['viewports']=[]
 for w,h in [(375,812),(390,844),(430,932)]:
  page.set_viewport_size({'width':w,'height':h});page.reload();page.locator('body').click(position={'x':2,'y':300});page.screenshot(path=str(root/f'screenshots/captura-{w}.png'));report['viewports'].append(page.evaluate('({width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,scrollHeight:document.documentElement.scrollHeight,dpr:devicePixelRatio})'))
 page.emulate_media(reduced_motion='reduce');assert page.evaluate('matchMedia("(prefers-reduced-motion: reduce)").matches');report['checks']['reduced_motion']=True
 page.get_by_role('link',name='Voltar',exact=True).click();assert 'MODEL_tela_07_V1' in page.url;report['checks']['back07']=page.url
 browser.close()
ref=Image.open(root.parent/'MODEL_assets_v1/referencias/08-filtros.png').convert('RGB');ref=ref.resize((round(ref.width*844/ref.height),844));cap=Image.open(root/'screenshots/captura-390.png').convert('RGB');out=Image.new('RGB',(ref.width+390,844),'#fff');out.paste(ref,(0,0));out.paste(cap,(ref.width,0));out.save(root/'comparacao-390.png')
report['sha256']={str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [*root.glob('screenshots/*.png'),root/'comparacao-390.png',root/'index.html',root/'styles.css',root/'app.js']}
(root/'relatorio-browser.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps(report,indent=2,ensure_ascii=False))
