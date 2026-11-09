#!/usr/bin/env python3
"""Faithful crop/alpha separation for MODEL04; never synthesize photographic pixels."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import json,hashlib,shutil,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'assets'
SOURCE=ROOT.parent/'MODEL_assets_v1/originais/mockup-geral.jpg'
full=Image.open(SOURCE).convert('RGB')
manifest={'source':'MODEL_assets_v1/originais/mockup-geral.jpg','sourceSha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'referencePanelCropLTRBExclusive':[634,0,826,404],'operation':'Crop original decoded RGB, modify only alpha to remove UI/frame regions, and set hidden RGB to zero. No synthesis, cloning, filling or resampling.','photos':{},'icons':{}}

def export_photo(name,box,mask,extra):
 photo=full.crop(box).convert('RGBA');photo.putalpha(mask)
 visible=hidden=0
 for y in range(photo.height):
  for x in range(photo.width):
   if mask.getpixel((x,y))==0:photo.putpixel((x,y),(0,0,0,0));hidden+=1
   else:visible+=1
 p=OUT/name;photo.save(p)
 original=full.crop(box)
 for y in range(photo.height):
  for x in range(photo.width):
   rgb=photo.getpixel((x,y))
   assert rgb[3] in(0,255)
   assert rgb[:3]==(original.getpixel((x,y)) if rgb[3] else (0,0,0))
 preview=Image.new('RGB',photo.size,'black');preview.paste(photo,mask=mask);preview.save(OUT/'previews'/(p.stem+'-preto.png'))
 mask.save(OUT/'previews'/(p.stem+'-alpha.png'))
 manifest['photos'][name]={'cropGlobalLTRBExclusive':list(box),'cropPanelLocalLTRBExclusive':[box[0]-634,box[1],box[2]-634,box[3]],'size':list(photo.size),'visiblePixelsSourceExact':visible,'transparentPixelsRgbZero':hidden,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),**extra}

# Correct monochrome hero of screen04, not the colour swipe portrait.
hero=full.crop((634,0,826,156))
mask=Image.new('L',hero.size,0);ImageDraw.Draw(mask).rounded_rectangle([0,0,191,167],radius=12,fill=255)
regions=[]
for name,box in [('status-time',[12,2,36,16]),('status-icons',[141,2,186,16]),('back',[10,22,27,43]),('options-uncertain',[164,21,186,43])]:
 glyph=Image.new('L',hero.size,0);seeds=0
 for y in range(box[1],box[3]+1):
  for x in range(box[0],box[2]+1):
   rgb=hero.getpixel((x,y))
   if min(rgb)>=90 and max(rgb)-min(rgb)<=35:
    glyph.putpixel((x,y),255);seeds+=1
 glyph=glyph.filter(ImageFilter.MaxFilter(3));mask.paste(0,(0,0),glyph)
 regions.append({'id':name,'searchBoxLTRBInclusive':box,'shape':'bright-ui-contour','rule':'minRGB>=90 && maxRGB-minRGB<=35','seedPixels':seeds,'maskedPixelsAfterDilation':glyph.histogram()[255],'dilationRadius':1})
ImageDraw.Draw(mask).rounded_rectangle([159,130,182,148],radius=9,fill=0)
regions.append({'id':'counter-1-of-8','shape':'rounded-rect','boxLTRBInclusive':[159,130,182,148],'radius':9,'note':'Whole pill UI removed; counter remains native UI, not eight supplied photos.'})
export_photo('hero-enzo-perfil.png',(634,0,826,156),mask,{'identity':'Monochrome hero from official panel04','alphaMasks':regions,'outerMask':{'shape':'top-rounded-panel','radius':12,'roundedRectExtendedBelowCrop':[0,0,191,167]},'limitations':'Status/controls/count have transparent holes; co-register native UI over them. Source photo has limited resolution; no missing pixels reconstructed.'})

thumbs=[('thumb-01.png',(639,157,690,205),1,False),('thumb-02.png',(693,157,745,205),2,False),('thumb-03.png',(748,157,800,205),1,False),('thumb-04-parcial.png',(803,157,826,205),1,True)]
for name,box,trim,partial in thumbs:
 w,h=box[2]-box[0],box[3]-box[1]
 alpha=Image.new('L',(w,h),0)
 bounds=[trim,trim,w+3 if partial else w-trim-1,h-trim-1]
 ImageDraw.Draw(alpha).rounded_rectangle(bounds,radius=3,fill=255)
 export_photo(name,box,alpha,{'partial':partial,'frameAlphaRemoval':{'roundedRectBoundsLTRBInclusive':bounds,'radius':3,'trimPixels':trim,'rightEdgeClipped':partial},'limitations':'Partial visible fourth image only, no hidden right side recovered.' if partial else 'Complete thumbnail as visible in panel; thin UI frame excluded by alpha.'})

# Reuse exact vector blobs only when the control matches.
for old,new in [('voltar.svg','voltar.svg'),('verificado.svg','verificado.svg')]:
 src=ROOT.parent/'MODEL_tela_03_V2/assets/icons'/old
 dst=OUT/'icons'/new;shutil.copyfile(src,dst)
 manifest['icons'][new]={'source':str(src.relative_to(ROOT.parent)),'reuse':'byte-identical copy','sha256':hashlib.sha256(dst.read_bytes()).hexdigest()}
icons={
 'opcoes.svg':'<path d="M12 3v3m0 12v3M3 12h3m12 0h3"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/>',
 'compartilhar.svg':'<path d="m15 4 5 5-5 5M20 9h-9a5 5 0 0 0-5 5"/><path d="M6 5H4a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>',
 'salvar.svg':'<path d="M6 3h12v18l-6-4-6 4z"/>',
 'aviao.svg':'<path d="m3 10 18-7-7 18-3-8z"/><path d="m11 13 10-10"/>',
}
for name,body in icons.items():
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{body}</svg>\n'
 p=OUT/'icons'/name;p.write_text(svg);ET.parse(p)
 manifest['icons'][name]={'source':'Manual vector approximation from small official panel04','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'uncertainty':'Top-right mark resembles a reticle/cross, not provably original options glyph; no visible label invented.' if name=='opcoes.svg' else 'Vector shape approximated; original vector unavailable.'}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({'photos':{name:{'size':v['size'],'sha256':v['sha256']} for name,v in manifest['photos'].items()},'icons':len(manifest['icons'])},ensure_ascii=False,indent=2))
