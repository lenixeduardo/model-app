#!/usr/bin/env python3
"""Second contour mask: preserve genuine sky/torso and zero hidden RGB, no synthesis."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'assets/derivados'
source_path=ROOT.parent/'MODEL_assets_v1/originais/mockup-geral.jpg'
source=Image.open(source_path).convert('RGB').crop((420,0,623,404))
alpha=Image.new('L',source.size,0)
d=ImageDraw.Draw(alpha);d.rounded_rectangle([0,0,202,403],radius=14,fill=255)
regions=[]

def remove_contour(name,box,kind):
 glyph=Image.new('L',source.size,0)
 selected=0
 for y in range(box[1],box[3]+1):
  for x in range(box[0],box[2]+1):
   r,g,b=source.getpixel((x,y));hi=max(r,g,b);lo=min(r,g,b)
   if kind=='label':
    hit=(hi>=120 and lo>=100 and hi-lo<=60) or (b>r+15 and g>r+15 and b>125)
   elif kind=='status':hit=hi>=120 and lo>=100 and hi-lo<=60
   elif kind=='info':hit=hi>=90 and lo>=75 and hi-lo<=45
   else:
    here=(r+g+b)/3
    up=sum(source.getpixel((x,y-3)))/3
    down=sum(source.getpixel((x,y+3)))/3
    hit=here-(up+down)/2>=9 and hi-lo<=80
   if hit:glyph.putpixel((x,y),255);selected+=1
 glyph=glyph.filter(ImageFilter.MaxFilter(3))
 alpha.paste(0,(0,0),glyph)
 regions.append({'id':name,'shape':'contour','searchBox':box,'rule':kind,'seedPixels':selected,'pixelsAfterDilation':glyph.histogram()[255],'dilationRadius':1})

remove_contour('status-hour',[14,2,44,17],'status')
remove_contour('status-icons',[151,2,195,17],'status')
remove_contour('progress',[12,21,191,26],'progress-local-contrast')
remove_contour('name-age-verification',[11,272,94,292],'label')
remove_contour('location-height',[11,292,118,307],'label')
remove_contour('information',[171,282,191,302],'info')
for name,box in [('Fashion',[12,311,60,331]),('Editorial',[61,311,110,331]),('Comercial',[112,311,170,331])]:
 ImageDraw.Draw(alpha).rounded_rectangle(box,radius=10,fill=0)
 regions.append({'id':'chip-'+name,'shape':'rounded-rect','box':box,'radius':10})
for name,cx in [('ignore',50),('favorite',101),('like',152)]:
 box=[cx-22,343,cx+22,387]
 ImageDraw.Draw(alpha).ellipse(box,fill=0)
 regions.append({'id':name,'shape':'ellipse','box':box,'center':[cx,365],'radius':22})
# Remove only the red JPEG fringe outside the circle; do not enlarge all three holes.
red_fringe=Image.new('L',source.size,0);red_count=0
for y in range(339,392):
 for x in range(126,179):
  r,g,b=source.getpixel((x,y))
  if r>16 and r>=g*1.8+5 and r>=b*1.3+3:
   red_fringe.putpixel((x,y),255);red_count+=1
red_fringe=red_fringe.filter(ImageFilter.MaxFilter(3))
alpha.paste(0,(0,0),red_fringe)
regions.append({'id':'like-jpeg-red-fringe','shape':'contour','searchBox':[126,339,178,391],'rule':'R>16 && R>=G*1.8+5 && R>=B*1.3+3','seedPixels':red_count,'pixelsAfterDilation':red_fringe.histogram()[255],'dilationRadius':1})
ImageDraw.Draw(alpha).rectangle([69,395,135,401],fill=0)
regions.append({'id':'home-indicator','shape':'rect','box':[69,395,135,401]})
result=source.convert('RGBA');result.putalpha(alpha)
visible=hidden=0
for y in range(404):
 for x in range(203):
  if alpha.getpixel((x,y))==0:
   result.putpixel((x,y),(0,0,0,0));hidden+=1
  else:visible+=1
name='enzo-painel03-mascarado-preciso2.png'
result.save(OUT/name);alpha.save(OUT/'enzo-painel03-alpha-preciso2.png')
for bg in ['preto','quadriculado']:
 preview=Image.new('RGB',source.size,'black' if bg=='preto' else '#e8e8e8')
 if bg=='quadriculado':
  q=ImageDraw.Draw(preview)
  for y in range(0,404,8):
   for x in range(0,203,8):
    if (x//8+y//8)%2:q.rectangle([x,y,x+7,y+7],fill='#bdbdbd')
 preview.paste(result,mask=alpha)
 preview.save(OUT/f'enzo-painel03-preview-{bg}-preciso2.png')
for y in range(404):
 for x in range(203):
  pixel=result.getpixel((x,y))
  assert pixel[3] in(0,255)
  assert pixel[:3]==(source.getpixel((x,y)) if pixel[3] else (0,0,0))
manifest={
 'source':'MODEL_assets_v1/originais/mockup-geral.jpg',
 'sourceSha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
 'cropLTRBExclusive':[420,0,623,404],'size':[203,404],
 'outerShape':{'shape':'rounded-rect','box':[0,0,202,403],'radius':14},
 'regions':regions,
 'rules':{
  'label':'(maxRGB>=120 && minRGB>=100 && maxRGB-minRGB<=60) OR (B>R+15 && G>R+15 && B>125)',
  'status':'maxRGB>=120 && minRGB>=100 && maxRGB-minRGB<=60',
  'info':'maxRGB>=90 && minRGB>=75 && maxRGB-minRGB<=45',
  'progress-local-contrast':'meanRGB(pixel)-average(meanRGB(y-3),meanRGB(y+3))>=9 && maxRGB-minRGB<=80; search only y21..26',
  'contourDilation':'MaxFilter(3), one pixel',
 },
 'operation':'Visible RGB copied byte-for-byte from decoded source; hidden RGB zero. Binary alpha masks only. No synthesis, filling, cloning or resampling.',
 'retainedPixels':visible,'transparentPixels':hidden,
 'previousPreciseRetainedPixels':66737,'additionalPreservedPixels':visible-66737,
 'outputs':{},
}
for p in [OUT/name,OUT/'enzo-painel03-alpha-preciso2.png',OUT/'enzo-painel03-preview-preto-preciso2.png',OUT/'enzo-painel03-preview-quadriculado-preciso2.png']:
 manifest['outputs'][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'enzo-painel03-proveniencia-precisa2.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(ROOT/'assets/enzo-mockup-foto-com-lacunas-precisas2.png').write_bytes((OUT/name).read_bytes())
(ROOT/'assets/mask-manifest-preciso2.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(manifest,ensure_ascii=False,indent=2))
