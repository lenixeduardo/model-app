#!/usr/bin/env python3
"""Uniform white UI paths with geometric AA only; no photographic RGB in SVG."""
from pathlib import Path
from PIL import Image,ImageFilter,ImageDraw
import json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'assets'
source=Image.open(ROOT.parent/'MODEL_assets_v1/originais/mockup-geral.jpg').convert('RGB').crop((420,0,623,404))
x1,y1,w,h=11,272,66,21
core=Image.new('L',(w,h),0)
for y in range(h):
 for x in range(w):
  p=source.getpixel((x+x1,y+y1))
  if max(p)>=120 and min(p)>=100 and max(p)-min(p)<=60:core.putpixel((x,y),255)
dilated=core.filter(ImageFilter.MaxFilter(3));ring=Image.new('L',(w,h),0)
for y in range(h):
 for x in range(w):
  if dilated.getpixel((x,y)) and not core.getpixel((x,y)):ring.putpixel((x,y),255)
def trace(mask):
 out=[]
 for y in range(h):
  x=0
  while x<w:
   if not mask.getpixel((x,y)):x+=1;continue
   start=x
   while x<w and mask.getpixel((x,y)):x+=1
   out.append(f'M{start} {y}h{x-start}v1H{start}z')
 return ''.join(out)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><defs><filter id="type-aa" x="-10%" y="-30%" width="120%" height="160%" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="0.35"/></filter></defs><g fill="#fafafa" filter="url(#type-aa)"><path opacity="0.2" d="{trace(ring)}"/><path d="{trace(core)}"/></g></svg>\n'''
p=OUT/'name-type.svg';p.write_text(svg)
ET.parse(p)
assert '<image' not in svg and 'href' not in svg
coverage=Image.new('L',(w,h),0)
coverage.paste(51,mask=ring);coverage.paste(255,mask=core)
coverage=coverage.filter(ImageFilter.GaussianBlur(.35))
preview=Image.new('RGB',(w*8,h*8),'#282828')
large=coverage.resize((w*8,h*8),Image.Resampling.BICUBIC)
preview.paste('#fafafa',mask=large)
preview.save(OUT/'derivados/name-type-aa-preview.png')
mp=OUT/'ui-type-manifest.json';m=json.loads(mp.read_text())
a=m['assets']['name-type.svg'];a['sha256']=hashlib.sha256(p.read_bytes()).hexdigest();a['supportPixels']={'opaqueCore':core.histogram()[255],'geometricRing':ring.histogram()[255]};a['geometricAA']={'onePixelRingOpacity':.2,'gaussianBlurStdDeviationSourceUnits':.35,'uniformFill':'#fafafa','noPhotographicRgb':True};a['photographicRemoval']='Photo precise2 uses one-pixel-dilated removal. This SVG has the identical225-pixel core contour plus the matching geometric one-pixel ring at20% opacity; the group is blurred0.35source units. Any halo/weight must be judged in actual browser capture.'
mp.write_text(json.dumps(m,ensure_ascii=False,indent=2))
print(json.dumps(a,ensure_ascii=False,indent=2))
