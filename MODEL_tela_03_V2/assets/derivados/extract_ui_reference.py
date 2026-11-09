#!/usr/bin/env python3
"""Independent foreground glyph rasters copied from source UI support only; no synthesis."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'assets/ui'
source_path=ROOT.parent/'MODEL_assets_v1/originais/mockup-geral.jpg'
photo_path=ROOT/'assets/enzo-mockup-foto-com-lacunas-precisas2.png'
source=Image.open(source_path).convert('RGB').crop((420,0,623,404))
photo=Image.open(photo_path).convert('RGBA')
photo_alpha=photo.getchannel('A')
manifest={
 'purpose':'Cycle7 candidate, independent foreground UI rasters for fixed reference labels, not approval or original font discovery.',
 'source':'MODEL_assets_v1/originais/mockup-geral.jpg',
 'sourceSha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
 'sourceCropLTRBExclusive':[420,0,623,404],
 'photo':'assets/enzo-mockup-foto-com-lacunas-precisas2.png',
 'photoSha256':hashlib.sha256(photo_path.read_bytes()).hexdigest(),
 'sourcePlane':[203,404],
 'operation':'Foreground alpha is the complement of precise2 photo alpha within each label box. Copy source RGB only for foreground alpha255; zero all transparent RGB. No resampling, generated pixels, hidden full rectangle or complete photograph in UI layer.',
 'contextMatte':'The existing one-pixel geometric dilation of UI core removal is retained as a contextual antialias matte copied from known source pixels. It may include the already-composited local backdrop at the glyph edge. No extra expansion beyond D was applied in this first candidate.',
 'integration':'Project source boxes using identical scale/cropOffset as photo. Keep native h1/p accessible and native font fallback. These fixed raster labels do not support arbitrary names/locales or identify the original font.',
 'labels':{},
}
composite=Image.new('RGBA',source.size,(0,0,0,255));composite.alpha_composite(photo)
for name,box in [('name-reference.png',[11,272,77,293]),('location-reference.png',[11,292,119,308])]:
 x1,y1,x2,y2=box;w=x2-x1;h=y2-y1
 fg=Image.new('RGBA',(w,h),(0,0,0,0));opaque=0
 for y in range(h):
  for x in range(w):
   if photo_alpha.getpixel((x+x1,y+y1))==0:
    fg.putpixel((x,y),(*source.getpixel((x+x1,y+y1)),255));opaque+=1
 p=OUT/name;fg.save(p)
 composite.alpha_composite(fg,(x1,y1))
 # Verify complete composition at native scale exactly recovers source pixels within the label box.
 local=Image.new('RGBA',(w,h),(0,0,0,255));local.alpha_composite(photo.crop(box));local.alpha_composite(fg)
 for y in range(h):
  for x in range(w):
   pixel=fg.getpixel((x,y))
   assert pixel[3] in(0,255)
   assert pixel[:3]==(source.getpixel((x+x1,y+y1)) if pixel[3] else (0,0,0))
   assert local.getpixel((x,y))[:3]==source.getpixel((x+x1,y+y1))
 # Independent layer previews, no complete photo inside the runtime foreground asset.
 preview=Image.new('RGB',(w,h),'#282828');preview.paste(fg,mask=fg.getchannel('A'))
 preview.resize((w*6,h*6),Image.Resampling.NEAREST).save(ROOT/'assets/derivados'/(p.stem+'-foreground-preview.png'))
 manifest['labels'][name]={
  'sourceBoxLTRBExclusive':box,'sourceBoxXYWH':[x1,y1,w,h],
  'size':[w,h],'opaquePixels':opaque,'totalPixels':w*h,'alphaFillFraction':opaque/(w*h),
  'contextMatteExpansionBeyondPhotoHole':0,'existingPhotoHoleDilationSourcePixels':1,
  'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
  'nativeCompositionMatchesSourceRgb':True,
  'foregroundVisibleRgbMatchesSourceRgb':True,'transparentRgbZero':True,
 }
composite.convert('RGB').save(ROOT/'assets/derivados/ui-reference-photo-composite-preview.png')
(OUT/'reference-type-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(manifest['labels'],ensure_ascii=False,indent=2))
