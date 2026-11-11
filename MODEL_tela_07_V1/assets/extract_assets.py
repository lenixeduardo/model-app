#!/usr/bin/env python3
"""Rebuild original Tela07 photo crops and verify provenance; requires Pillow."""
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw
import hashlib, json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SOURCE=ROOT/'MODEL_assets_v1/originais/mockup-geral.jpg'
REFERENCE=ROOT/'MODEL_assets_v1/referencias/07-castings.png'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
source=Image.open(SOURCE).convert('RGB')
reference=Image.open(REFERENCE).convert('RGB')
panel=(11,434,212,751)
assert ImageChops.difference(source.crop(panel),reference).getbbox() is None
specs=[('campanha-inverno-2025.png',(12,65,74,124),'Homem de cabelo escuro, casaco preto aberto, fundo cinza.'),('marca-esportiva.png',(12,140,74,204),'Homem de cabelo curto e regata escura; região dos olhos sombreada, óculos não confirmáveis.'),('editorial-masculino.png',(12,218,74,283),'Homem de cabelo escuro, camisa clara aberta, fundo cinza escuro.')]
photos=[]
for name,local,description in specs:
 box=tuple(v+panel[i%2] for i,v in enumerate(local))
 crop=source.crop(box)
 mask=Image.new('L',crop.size,0)
 ImageDraw.Draw(mask).rounded_rectangle((0,0,crop.width-1,crop.height-1),radius=5,fill=255)
 out=crop.convert('RGBA');out.putalpha(mask)
 pixels=out.load();original=crop.load();visible=hidden=0
 for y in range(out.height):
  for x in range(out.width):
   if pixels[x,y][3]:
    assert pixels[x,y][:3]==original[x,y];visible+=1
   else: pixels[x,y]=(0,0,0,0);hidden+=1
 path=HERE/name;out.save(path)
 reopened=Image.open(path)
 assert all(p[:3]==(0,0,0) for p in reopened.getdata() if p[3]==0)
 photos.append(dict(file=name,description=description,local_box=list(local),source_box=list(box),dimensions=list(out.size),sha256=sha(path),crop_rgb_sha256=hashlib.sha256(crop.tobytes()).hexdigest(),visible_pixels=visible,transparent_pixels=hidden,visible_rgb_identical=True,transparent_rgb_zero=True,mask='Binary geometric rounded rectangle, radius5 source pixels; no resampling',complete_visible_frame=True))
icons=[]
for path in sorted(HERE.glob('*.svg')):
 entry=dict(file=path.name,sha256=sha(path),classification='Local approximate vector; no source raster pixels')
 for previous in [ROOT/'MODEL_tela_06_V1/assets'/path.name,ROOT/'MODEL_tela_04_V1/assets/icons/salvar.svg']:
  if previous.exists() and sha(previous)==sha(path):entry['copied_from']=str(previous.relative_to(ROOT))
 icons.append(entry)
manifest=dict(source=dict(file=str(SOURCE.relative_to(ROOT)),sha256=sha(SOURCE),dimensions=list(source.size)),reference=dict(file=str(REFERENCE.relative_to(ROOT)),sha256=sha(REFERENCE),dimensions=list(reference.size),source_box=list(panel),rgb_identical=True),photos=photos,icons=icons,limitations=['Low resolution JPEG; source matte/compression retained; no recovered or generated pixels.','No titles, labels, dates, fee values or UI rasterized into photo assets.','Faces and bodies remain source-only; original three frames are independent.'])
(HERE/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(panel_rgb_identical=True,photos=[dict(file=p['file'],dimensions=p['dimensions'],visible_rgb_identical=p['visible_rgb_identical'],transparent_rgb_zero=p['transparent_rgb_zero']) for p in photos],icons=len(icons)),ensure_ascii=False))
