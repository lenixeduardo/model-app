#!/usr/bin/env python3
"""Refine only text/seal holes from the conservative alpha; never fill/synthesize photo."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'assets/derivados'
source_path=ROOT.parent/'MODEL_assets_v1/originais/mockup-geral.jpg'
source=Image.open(source_path).convert('RGB').crop((420,0,623,404))
alpha=Image.open(OUT/'enzo-painel03-alpha.png').convert('L')
regions=[{'id':'name-age-verification','box':[11,272,94,292]},{'id':'location-height','box':[11,292,118,307]}]
counts=[]
for reg in regions:
 ImageDraw.Draw(alpha).rectangle(reg['box'],fill=255)
 glyph=Image.new('L',source.size,0)
 selected=0
 x1,y1,x2,y2=reg['box']
 for y in range(y1,y2+1):
  for x in range(x1,x2+1):
   r,g,b=source.getpixel((x,y));hi=max(r,g,b);lo=min(r,g,b)
   neutral=hi>=120 and lo>=100 and hi-lo<=60
   blue=b>r+15 and g>r+15 and b>125
   if neutral or blue: glyph.putpixel((x,y),255);selected+=1
 glyph=glyph.filter(ImageFilter.MaxFilter(3))
 alpha.paste(0,(0,0),glyph)
 counts.append({**reg,'selectedSeedPixels':selected,'maskedAfterDilation':glyph.histogram()[255]})
result=source.convert('RGBA');result.putalpha(alpha)
# Erase only invisible RGB so the PNG contains no hidden UI payload.
for y in range(404):
 for x in range(203):
  if alpha.getpixel((x,y))==0: result.putpixel((x,y),(0,0,0,0))
name='enzo-painel03-mascarado-preciso.png'
result.save(OUT/name)
alpha.save(OUT/'enzo-painel03-alpha-preciso.png')
for bg in ['preto','quadriculado']:
 preview=Image.new('RGB',source.size,'black' if bg=='preto' else '#e8e8e8')
 if bg=='quadriculado':
  d=ImageDraw.Draw(preview)
  for y in range(0,404,8):
   for x in range(0,203,8):
    if (x//8+y//8)%2:d.rectangle([x,y,x+7,y+7],fill='#bdbdbd')
 preview.paste(result,mask=alpha)
 preview.save(OUT/f'enzo-painel03-preview-{bg}-preciso.png')
retained=0
for y in range(404):
 for x in range(203):
  pix=result.getpixel((x,y))
  assert pix[:3]==(source.getpixel((x,y)) if pix[3]==255 else (0,0,0))
  assert pix[3] in(0,255)
  retained+=pix[3]==255
manifest={
 'source':'MODEL_assets_v1/originais/mockup-geral.jpg',
 'sourceSha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
 'cropLTRBExclusive':[420,0,623,404], 'size':[203,404],
 'baseMask':'assets/derivados/enzo-painel03-alpha.png',
 'baseMaskSha256':hashlib.sha256((OUT/'enzo-painel03-alpha.png').read_bytes()).hexdigest(),
 'precisionRegions':counts,
 'selectionRule':'Within the two label bounding boxes only: (maxRGB>=120 && minRGB>=100 && maxRGB-minRGB<=60) OR (B>R+15 && G>R+15 && B>125). Dilate selected UI contours by one pixel using MaxFilter(3).',
 'operation':'Visible RGB (alpha255) copied byte-for-byte from decoded source; hidden RGB (alpha0) set to zero. Alpha mask unchanged. No photo synthesis, interpolation, cloning or filling.',
 'retainedPixels':retained,'transparentPixels':203*404-retained,
 'retainedPixelsConservative':64634,'additionalPreservedPixels':retained-64634,
 'outputs':{},
}
for p in [OUT/name,OUT/'enzo-painel03-alpha-preciso.png',OUT/'enzo-painel03-preview-preto-preciso.png',OUT/'enzo-painel03-preview-quadriculado-preciso.png']:
 manifest['outputs'][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'enzo-painel03-proveniencia-precisa.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(ROOT/'assets/enzo-mockup-foto-com-lacunas-precisas.png').write_bytes((OUT/name).read_bytes())
(ROOT/'assets/mask-manifest-preciso.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(manifest,ensure_ascii=False,indent=2))
