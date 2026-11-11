"""Reproduce only vector copies, provenance and source color sampling; no UI raster."""
from pathlib import Path
from PIL import Image, ImageChops
from collections import Counter
import hashlib, json, shutil
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source=ROOT/'MODEL_assets_v1/originais/mockup-geral.jpg'
reference=ROOT/'MODEL_assets_v1/referencias/08-filtros.png'
src=Image.open(source).convert('RGB'); ref=Image.open(reference).convert('RGB')
box=[220,434,420,751]
assert src.size==(1179,753) and ref.size==(200,317)
assert ImageChops.difference(src.crop(box),ref).getbbox() is None
copies={'back.svg':'MODEL_tela_06_V1/assets/back.svg','location.svg':'MODEL_tela_07_V1/assets/search.svg',**{n+'.svg':'MODEL_tela_06_V1/assets/'+n+'.svg' for n in ['cellular','wifi','battery']}}
for name,origin in copies.items(): shutil.copyfile(ROOT/origin,OUT/name)
(OUT/'chevron.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round" role="img" aria-labelledby="title"><title id="title">Expandir distância</title><path d="m7 10 5 5 5-5"/></svg>\n')
regions={'paper':[70,35,120,42],'text':[80,284,125,296],'field':[35,57,120,61],'track':[105,102,180,105],'secondary':[128,89,185,94],'black':[25,283,65,296]}
samples={}
for name,b in regions.items():
 pixels=list(ref.crop(b).getdata()); rgb,count=Counter(pixels).most_common(1)[0]
 samples[name]={'local_box':b,'method':'most frequent exact RGB; text patch includes antialias/background','rgb':list(rgb),'hex':'#%02x%02x%02x'%rgb,'count':count}
# Dark ink estimated from dark-only pixels in title; gray ink from gray-only value pixels.
for name,b,lo,hi in [('text',[81,21,111,31],0,80),('secondary',[128,89,185,94],70,180)]:
 pixels=[p for p in ref.crop(b).getdata() if lo<=sum(p)/3<=hi]
 rgb,count=Counter(pixels).most_common(1)[0]
 samples[name]={'local_box':b,'method':f'most frequent RGB with mean channel in [{lo},{hi}]','rgb':list(rgb),'hex':'#%02x%02x%02x'%rgb,'count':count}
icons=[]
for p in sorted(OUT.glob('*.svg')):
 item={'file':p.name,'sha256':sha(p),'classification':'Approximate local vector, no raster source pixels','viewBox':[0,0,24,24]}
 if p.name in copies: item.update(copied_from=copies[p.name],origin_sha256=sha(ROOT/copies[p.name]),byte_identical=True)
 icons.append(item)
data={'source':{'file':str(source.relative_to(ROOT)),'sha256':sha(source),'dimensions':list(src.size)},'reference':{'file':str(reference.relative_to(ROOT)),'sha256':sha(reference),'dimensions':list(ref.size),'source_box':box,'rgb_identical':True,'difference_bbox':None},'photos':[],'photography_criterion':'N/A; normalize remaining 65% as DESIGN_SPEC.md','color_samples':samples,'icons':icons,'limitations':['JPEG and low resolution; vectors are approximations, not exact tracing.','location.svg represents the magnifying glass visible at field start, not a pin.','All labels, status time, chips, controls, tracks and handles must be native HTML/CSS; no full-reference background.']}
(OUT/'manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_crop':box,'colors':{k:v['hex'] for k,v in samples.items()},'icons':len(icons)},ensure_ascii=False))
