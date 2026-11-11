from pathlib import Path
from PIL import Image
import hashlib,json
p=Path(__file__).parent
r=Image.open(p.parent/'MODEL_assets_v1/referencias/11-notificacoes.png').convert('RGB');r=r.resize((round(r.width*844/r.height),844))
a=Image.open(p/'captura-390.png').convert('RGB');c=Image.new('RGB',(r.width+a.width,844),'white');c.paste(r,(0,0));c.paste(a,(r.width,0));c.save(p/'comparacao-390.png')
files=sorted(x for x in p.rglob('*') if x.is_file() and x.name not in ['EVIDENCIAS.json','SHA256SUMS'])
hashes={str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
report=json.loads((p/'browser-report.json').read_text())
e={'version':(p/'VERSION').read_text().strip(),'browser':report['browser'],'device_scale_factor':1,'initial_test':'PASS before HTML: five genuine photo contracts and ten SVG assets; source test is intentionally preimplementation only','commands':['./MODEL_tela_11_V1/serve.sh','node MODEL_tela_11_V1/verify.cjs --candidate','node MODEL_tela_11_V1/verify.cjs','python MODEL_tela_11_V1/evidence.py'],'captures':[{'file':f'captura-{w}.png','width':w,'height':h,'opened_visually':True}for w,h in [(375,812),(390,844),(430,932)]],'candidate_opened_before_finals':True,'comparison':{'file':'comparacao-390.png','reference':[490,844],'app':[390,844],'proportions_preserved':True,'opened_visually':True},'browser_report':'browser-report.json','limits':['Arial and vector icons are approximations','JPEG photos have only 28x28 original pixels','No remote identity, taxonomy or read state inferred','Target viewport heights >=660; no general desktop redesign claimed'],'auditor_score':None,'sha256':hashes}
(p/'EVIDENCIAS.json').write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')
hashes['EVIDENCIAS.json']=hashlib.sha256((p/'EVIDENCIAS.json').read_bytes()).hexdigest()
(p/'SHA256SUMS').write_text(''.join(f'{v}  {k}\n'for k,v in sorted(hashes.items())))
print('Evidence generated',len(hashes),'hashes')
