#!/usr/bin/env python3
"""Reproduce only original photo crops and justified local SVGs; no image synthesis."""
from pathlib import Path
from PIL import Image, ImageChops
import hashlib, json, math, shutil
from collections import Counter
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
source=ROOT/'MODEL_assets_v1/originais/mockup-geral.jpg'
ref=ROOT/'MODEL_assets_v1/referencias/09-salvos.png'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
im=Image.open(source).convert('RGB'); panel=im.crop((428,434,604,751))
assert ImageChops.difference(panel,Image.open(ref).convert('RGB')).getbbox() is None
photos=[]
for ident,name,age,city,box,center in [
 ('enzo','Enzo',26,'São Paulo, SP',(12,72,86,135),(77,126)),
 ('gabriel','Gabriel',28,'Rio de Janeiro, RJ',(92,72,166,135),(157,126)),
 ('rafael','Rafael',29,'São Paulo, SP',(12,168,86,233),(77,224)),
 ('theo','Theo',24,'Belo Horizonte, MG',(92,168,166,233),(157,224))]:
 x0,y0,x1,y1=box; w=x1-x0; h=y1-y0; cx,cy=center[0]-x0,center[1]-y0
 rgb=panel.crop(box); rgba=rgb.convert('RGBA'); radius=9.5; corner=5.0; hidden=0; visible=0
 for y in range(h):
  for x in range(w):
   px,py=x+.5,y+.5
   qx=max(corner-px,0,px-(w-corner)); qy=max(corner-py,0,py-(h-corner))
   outside=qx*qx+qy*qy>corner*corner
   control=(px-cx)**2+(py-cy)**2<=radius**2
   if outside or control: rgba.putpixel((x,y),(0,0,0,0)); hidden+=1
   else: assert rgba.getpixel((x,y))[:3]==rgb.getpixel((x,y)); visible+=1
 path=OUT/f'{ident}.png'; rgba.save(path)
 # Opaque footprint extends .25 source px beyond removed disk: coverage in either state.
 # Both are clipped by the photo's original corner when composed by the implementation.
 samples=[rgb.getpixel((x,y)) for y in range(h) for x in range(w)
          if 6<math.hypot(x+.5-cx,y+.5-cy)<8.5 and x<cx-2]
 color=tuple(sorted(p[c] for p in samples)[len(samples)//2] for c in range(3))
 fill='#%02x%02x%02x'%color
 for saved in (True,False):
  state='saved' if saved else 'unsaved'; title='Remover dos salvos' if saved else 'Salvar modelo'
  glyph=f'<path d="M-3-4h6v8L0 2-3 4Z" fill="{chr(35)+"fff" if saved else "none"}" stroke="#fff" stroke-width=".8" stroke-linejoin="round"/>'
  (OUT/f'bookmark-{ident}-{state}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -10 20 20" role="img" aria-labelledby="title"><title id="title">{title}</title><circle r="9.75" fill="{fill}"/>{glyph}</svg>\n')
 photos.append(dict(file=path.name,identity=name,age=age,city=city,local_box=list(box),global_box=[x0+428,y0+434,x1+428,y1+434],width=w,height=h,aspect_ratio=w/h,sha256=sha(path),visible_rgb_equal_source=True,transparent_rgb_zero=True,visible_pixels=visible,hidden_pixels=hidden,corner_radius=corner,control=dict(center_local_panel=list(center),center_relative_photo=[cx,cy],center_fraction=[cx/w,cy/h],mask_radius=radius,mask_bbox_relative=[cx-radius,cy-radius,cx+radius,cy+radius],svg_diameter=20,opaque_circle_radius=9.75,fill=fill,coverage_both_states=True)))
icons=[]
for file,folder in [('nav-home.svg','07'),('search.svg','07'),('plus.svg','07'),('chat.svg','07'),('profile.svg','07'),('cellular.svg','06'),('wifi.svg','06'),('battery.svg','06')]:
 p=ROOT/f'MODEL_tela_{folder}_V1/assets'/file; shutil.copyfile(p,OUT/file)
 icons.append(dict(file=file,source=str(p.relative_to(ROOT)),sha256=sha(OUT/file),byte_identical=True))
(OUT/'options.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-labelledby="title"><title id="title">Opções de salvos</title><g fill="currentColor"><circle cx="12" cy="4" r="1.5"/><circle cx="12" cy="20" r="1.5"/><circle cx="4" cy="12" r="1.5"/><circle cx="20" cy="12" r="1.5"/><path d="M11 7h2v10h-2zM7 11h10v2H7z"/></g></svg>\n')
colors={}
for key,box in [('paper',[5,35,170,44]),('lower_paper',[10,260,165,280]),('active_tab',[20,50,80,58]),('secondary_text',[94,153,153,159])]:
 hist=Counter(panel.crop(box).getdata()); value,count=hist.most_common(1)[0]
 colors[key]=dict(box=box,mode_rgb=value,mode_hex='#%02x%02x%02x'%value,count=count,uncertainty='JPEG pixels; secondary region includes paper, not an isolated font color' if key=='secondary_text' else 'JPEG variation')
# Gray text sampled from dark glyph core, avoiding background: not a semantic brand token.
colors['secondary_glyph_pixel']=dict(coordinate=[97,155],rgb=panel.getpixel((97,155)),hex='#%02x%02x%02x'%panel.getpixel((97,155)))
manifest=dict(source=dict(file=str(source.relative_to(ROOT)),sha256=sha(source),dimensions=im.size),reference=dict(file=str(ref.relative_to(ROOT)),sha256=sha(ref),dimensions=panel.size,global_box=[428,434,604,751],rgb_identical=True),photos=photos,icons=icons,colors=colors,mask_rule='Evaluate pixel centers (x+.5,y+.5); remove circle radius9.5 and outside rounded rectangle radius5. No RGB changes for alpha>0. Alpha is binary; hidden RGB=0. Control disk radius9.75 covers mask in saved and unsaved SVG. Clip UI at same photo frame/corners.',limitations=['Original JPEG only; no unseen photo pixels recovered.','Four identities assigned strictly from labels; Gabriel clothing differs from prose description: actual original sleeveless gray top retained.','UI footprint/corner geometry approximate ±1 source pixel; JPEG matte may remain.','Opaque controls approximate original translucent overlays; each fill sampled from original left annulus.','No source font available; use native Arial/Helvetica text, never raster labels.'])
manifest['generated_files']={p.name:sha(p) for p in sorted(OUT.iterdir()) if p.suffix in ('.png','.svg')}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'photos':[(p['file'],p['width'],p['height'],p['visible_pixels']) for p in photos],'panel_rgb_identical':True,'all_visible_rgb_preserved':True,'hidden_rgb_zero':True,'coverage_both_states':True,'colors':colors},ensure_ascii=False,indent=2))
