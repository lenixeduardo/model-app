#!/usr/bin/env python3
"""Capture and verify the actual local UI. Requires playwright, Pillow and Chromium."""
import argparse
import functools
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--chromium', default='/usr/bin/chromium')
    parser.add_argument('--out', type=Path, default=ROOT)
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{server.server_port}/'
    report = {'url': url, 'deviceScaleFactor': 1, 'viewports': [], 'checks': []}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=args.chromium, headless=True, args=['--no-sandbox'])
            report['browser'] = browser.version
            for width, height in [(375,812), (390,844), (430,932)]:
                context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1, is_mobile=True, has_touch=True)
                page = context.new_page()
                errors, failures = [], []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
                page.on('requestfailed', lambda req: failures.append({'url': req.url, 'error': req.failure}))
                page.on('response', lambda res: failures.append({'url': res.url, 'status': res.status}) if res.status >= 400 else None)
                response = page.goto(url, wait_until='networkidle')
                assert response.status == 200, f'Expected implemented index.html (200), got {response.status}'
                assert page.title() == 'Enzo, 26 — MODEL'
                page.evaluate('document.fonts.ready')
                state = page.evaluate('''() => ({viewport:[innerWidth,innerHeight], document:[document.documentElement.scrollWidth,document.documentElement.scrollHeight], font: getComputedStyle(document.querySelector('h1')).fontFamily, images:[...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0,natural:[i.naturalWidth,i.naturalHeight],rendered:[i.width,i.height]})), targets:[...document.querySelectorAll('button:not([hidden])')].filter(b=>b.getClientRects().length).map(b=>({label:b.getAttribute('aria-label')||b.textContent.trim(),width:b.getBoundingClientRect().width,height:b.getBoundingClientRect().height}))})''')
                assert state['document'] == [width,height], state
                assert all(i['loaded'] for i in state['images']), state
                assert all(b['width']>=44 and b['height']>=44 for b in state['targets']), state['targets']
                assert page.locator('.progress span').count() == 5
                portrait = next(i for i in state['images'] if 'enzo-' in i['src'])
                nr = portrait['natural'][0]/portrait['natural'][1]
                rr = portrait['rendered'][0]/portrait['rendered'][1]
                assert abs(nr-rr)<0.01, portrait
                shot = out / f'captura-{width}.png'
                page.screenshot(path=str(shot), full_page=True)
                for label in ['Favoritar Enzo', 'Curtir Enzo']:
                    button = page.get_by_role('button', name=label, exact=True)
                    button.tap(); assert button.get_attribute('aria-pressed') == 'true'
                    button.tap(); assert button.get_attribute('aria-pressed') == 'false'
                page.get_by_role('button', name='Ignorar Enzo', exact=True).tap()
                assert page.get_by_role('heading', name='Perfil ignorado').is_visible()
                page.get_by_role('button', name='Desfazer', exact=True).tap()
                assert page.get_by_role('heading', name='Enzo, 26').is_visible()
                page.get_by_role('button', name='Mais opções', exact=True).tap()
                assert page.get_by_role('dialog').is_visible()
                page.keyboard.press('Escape')
                assert not page.get_by_role('dialog').is_visible()
                page.get_by_role('button', name='Informações sobre Enzo', exact=True).tap()
                assert page.get_by_role('dialog').is_visible()
                page.get_by_role('button', name='Fechar', exact=True).tap()
                page.get_by_role('button', name='Voltar', exact=True).tap()
                assert page.get_by_role('dialog').is_visible()
                page.keyboard.press('Escape')
                page.keyboard.press('Tab')
                focus = page.evaluate('''() => ({tag:document.activeElement.tagName,outline:getComputedStyle(document.activeElement).outlineStyle})''')
                assert focus['tag'] == 'BUTTON' and focus['outline'] != 'none', focus
                assert not errors and not failures, {'console':errors,'network':failures}
                report['viewports'].append({'width':width,'height':height,'state':state,'consoleErrors':errors,'networkErrors':failures,'screenshot':shot.name,'sha256':hashlib.sha256(shot.read_bytes()).hexdigest(),'interactions':'passed','keyboardFocus':focus})
                context.close()
            page = browser.new_page(viewport={'width':390,'height':844}, reduced_motion='reduce')
            page.goto(url, wait_until='networkidle')
            page.get_by_role('button', name='Curtir Enzo', exact=True).click()
            assert page.get_by_role('button', name='Curtir Enzo', exact=True).get_attribute('aria-pressed')=='true'
            report['checks'].append('Reduced motion: interaction works')
            page.close()
            page = browser.new_page(viewport={'width':390,'height':844})
            page.route('**/enzo-swipe-referencia.png', lambda route: route.abort())
            page.goto(url, wait_until='networkidle')
            assert page.get_by_role('status').filter(has_text='Não foi possível carregar a fotografia.').is_visible()
            assert page.get_by_role('button',name='Curtir Enzo',exact=True).is_disabled()
            report['checks'].append('Missing portrait: visible fallback and actions disabled')
            browser.close()
        report['result'] = 'passed'
    finally:
        server.shutdown(); server.server_close()
        (out/'relatorio-browser.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps({'result':report.get('result'),'browser':report.get('browser'),'viewports':len(report['viewports']),'checks':report['checks']},ensure_ascii=False))

if __name__=='__main__':
    main()
