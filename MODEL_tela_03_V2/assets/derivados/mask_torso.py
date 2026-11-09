#!/usr/bin/env python3
"""Geometric crop/mask only: never synthesize or interpolate hidden photo pixels."""
from pathlib import Path
from PIL import Image, ImageDraw
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT.parent/'MODEL_assets_v1/originais/mockup-geral.jpg'
OUT=ROOT/'assets/derivados'
CROP=(420,0,623,404)
regions=[
 {'id':'status-hour','shape':'rect','box':[14,2,44,17]},
 {'id':'status-icons','shape':'rect','box':[151,2,195,17]},
 {'id':'progress','shape':'rect','box':[12,20,191,28]},
 {'id':'name-age-verification','shape':'rect','box':[11,272,94,292]},
 {'id':'location-height','shape':'rect','box':[11,292,118,307]},
 {'id':'information','shape':'ellipse','box':[170,281,192,303]},
 {'id':'chip-fashion','shape':'rounded-rect','box':[11,310,60,333],'radius':10},
 {'id':'chip-editorial','shape':'rounded-rect','box':[62,310,111,333],'radius':10},
 {'id':'chip-comercial','shape':'rounded-rect','box':[113,310,176,333],'radius':10},
 {'id':'ignore','shape':'ellipse','box':[26,340,75,390]},
 {'id':'favorite','shape':'ellipse','box':[77,340,126,390]},
 {'id':'like','shape':'ellipse','box':[128,340,178,390]},
 {'id':'home-indicator','shape':'rect','box':[66,392,139,403]},
]
source=Image.open(SOURCE).convert('RGB').crop(CROP)
mask=Image.new('L',source.size,0)
d=ImageDraw.Draw(mask)
d.rounded_rectangle([0,0,202,403],radius=14,fill=255)
for reg in regions:
 if reg['shape']=='rect': d.rectangle(reg['box'],fill=0)
 elif reg['shape']=='ellipse': d.ellipse(reg['box'],fill=0)
 else: d.rounded_rectangle(reg['box'],radius=reg['radius'],fill=0)
result=source.convert('RGBA');result.putalpha(mask)
result.save(OUT/'enzo-painel03-mascarado.png')
mask.save(OUT/'enzo-painel03-alpha.png')
preview=Image.new('RGB',source.size,'black');preview.paste(result,mask=result.getchannel('A'))
preview.save(OUT/'enzo-painel03-preview-preto.png')
checker=Image.new('RGB',source.size,'#e8e8e8');cd=ImageDraw.Draw(checker)
for cy in range(0,source.height,8):
 for cx in range(0,source.width,8):
  if (cx//8+cy//8)%2: cd.rectangle([cx,cy,cx+7,cy+7],fill='#bdbdbd')
checker.paste(result,mask=result.getchannel('A'))
checker.save(OUT/'enzo-painel03-preview-quadriculado.png')
# Explicitly verify that every surviving pixel is a source pixel, with no interpolation.
retained=0;transparent=0
for y in range(source.height):
 for x in range(source.width):
  pixel=result.getpixel((x,y))
  assert pixel[:3]==source.getpixel((x,y))
  assert pixel[3] in (0,255)
  retained+=pixel[3]==255;transparent+=pixel[3]==0
records={
 'source':str(SOURCE.relative_to(ROOT.parent)),
 'sourceSha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'cropLTRBExclusive':list(CROP),'size':[203,404],
 'coordinateConvention':'crop right/bottom exclusive; mask boxes use Pillow inclusive endpoints',
 'outerShape':{'shape':'rounded-rect','box':[0,0,202,403],'radius':14},
 'uiRegionsRemoved':regions,
 'operation':'RGB copied byte-for-byte from decoded source crop; binary alpha mask, no inpainting, no generation, no resampling',
 'retainedPixels':retained,'transparentPixels':transparent,
 'outputs':{},
}
for name in ['enzo-painel03-mascarado.png','enzo-painel03-alpha.png','enzo-painel03-preview-preto.png','enzo-painel03-preview-quadriculado.png']:
 records['outputs'][name]=hashlib.sha256((OUT/name).read_bytes()).hexdigest()
(OUT/'enzo-painel03-proveniencia.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
# Vector control mask matches the raster alpha geometry. It contains no photo.
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="203" height="404" viewBox="0 0 203 404"><defs><mask id="photo" maskUnits="userSpaceOnUse"><rect width="203" height="404" fill="black"/><rect x="0" y="0" width="203" height="404" rx="14" fill="white"/>']
for reg in regions:
 x1,y1,x2,y2=reg['box']
 if reg['shape']=='ellipse': parts.append(f'<ellipse cx="{(x1+x2)/2}" cy="{(y1+y2)/2}" rx="{(x2-x1+1)/2}" ry="{(y2-y1+1)/2}" fill="black"/>')
 else:
  radius=reg.get('radius',0)
  parts.append(f'<rect x="{x1}" y="{y1}" width="{x2-x1+1}" height="{y2-y1+1}" rx="{radius}" fill="black"/>')
parts.append('</mask></defs><rect width="203" height="404" fill="white" mask="url(#photo)"/></svg>')
(OUT/'enzo-painel03-mascara.svg').write_text(''.join(parts)+'\n')
print(json.dumps({'retainedPixels':retained,'transparentPixels':transparent,'outputs':records['outputs']},indent=2))
