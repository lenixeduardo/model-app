#!/usr/bin/env python3
"""Trace UI glyph support as uniform SVG paths, never copy photographic RGB into UI."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'assets'
source_path=ROOT.parent/'MODEL_assets_v1/originais/mockup-geral.jpg'
source=Image.open(source_path).convert('RGB').crop((420,0,623,404))
manifest={'source':'MODEL_assets_v1/originais/mockup-geral.jpg','sourceSha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),'sourceCropLTRBExclusive':[420,0,623,404],'sourcePlane':[203,404],'operation':'Binary UI contour support traced as uniform-fill SVG paths. No photographic RGB, image element, raster payload, font discovery or anatomy reconstruction.','positioning':'u=viewportHeight/404; image width=203*u; cropOffsetX=(imageWidth-viewportWidth)*0.08; SVG left=x*u-cropOffsetX, top=y*u, width=w*u, height=h*u. Bounds are inclusive in the source; local viewBox starts at0,0.','assets':{}}

def trace(mask):
 commands=[]
 for y in range(mask.height):
  x=0
  while x<mask.width:
   if not mask.getpixel((x,y)):x+=1;continue
   start=x
   while x<mask.width and mask.getpixel((x,y)):x+=1
   commands.append(f'M{start} {y}h{x-start}v1H{start}z')
 return ''.join(commands)

def export(name,box,layers):
 x1,y1,x2,y2=box;w=x2-x1+1;h=y2-y1+1;parts=[];counts={}; previews=[]
 for layer_name,fill,predicate in layers:
  mask=Image.new('L',(w,h),0)
  for y in range(h):
   for x in range(w):
    if predicate(source.getpixel((x+x1,y+y1))):mask.putpixel((x,y),255)
  counts[layer_name]=mask.histogram()[255]
  parts.append(f'<path fill="{fill}" d="{trace(mask)}"/>')
  previews.append((mask,fill))
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{"".join(parts)}</svg>\n'
 p=OUT/(name+'.svg');p.write_text(svg)
 tree=ET.parse(p)
 assert all(e.tag.rsplit('}',1)[-1] in['svg','path'] for e in tree.iter())
 assert 'image' not in svg and 'href' not in svg
 preview=Image.new('RGB',(w,h),'#282828')
 for mask,fill in previews:preview.paste(fill,mask=mask)
 preview.resize((w*6,h*6),Image.Resampling.NEAREST).save(ROOT/'assets/derivados'/(name+'-preview.png'))
 manifest['assets'][name+'.svg']={'sourceBoxXYWH':[x1,y1,w,h],'sourceBoxLTRBInclusive':box,'viewBox':[0,0,w,h],'supportPixels':counts,'fills':[fill for _,fill,_ in layers],'dilation':0,'photographicRemoval':'The photograph precise2 has one-pixel-dilated removal support around these source glyphs; this UI paints only original core contour support, never the699-pixel enlarged name hole. Any remaining halo must be judged in the browser.','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 return previews

def neutral(rgb):return max(rgb)>=120 and min(rgb)>=100 and max(rgb)-min(rgb)<=60
name_layers=export('name-type',[11,272,76,292],[('text','#fafafa',neutral)])
location_layers=export('location-type',[11,292,118,307],[('text','#eeece9',neutral)])
verification_layers=export('verification-type',[76,272,94,292],[('badge','#69b9f1',lambda rgb:rgb[2]>rgb[0]+15 and rgb[1]>rgb[0]+15 and rgb[2]>125),('check','#ffffff',lambda rgb:rgb[0]>=170 and rgb[1]>=180 and rgb[2]>=190)])
# Non-runtime preview composite: photo mask over black plus these independent visual UI layers.
base=Image.open(OUT/'enzo-mockup-foto-com-lacunas-precisas2.png').convert('RGBA')
composite=Image.new('RGB',(203,404),'black');composite.paste(base,mask=base.getchannel('A'))
for box,layers in [([11,272,76,292],name_layers),([11,292,118,307],location_layers),([76,272,94,292],verification_layers)]:
 for mask,fill in layers:composite.paste(fill,(box[0],box[1]),mask)
composite.save(ROOT/'assets/derivados/ui-type-photo-composite-preview.png')
(OUT/'ui-type-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(manifest,ensure_ascii=False,indent=2))
