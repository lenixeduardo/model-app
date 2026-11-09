#!/usr/bin/env python3
"""Rebuild faithful source crops and documented vector approximations; Pillow only."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageChops
import hashlib, json, math
BASE=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SOURCE=BASE/'MODEL_assets_v1/originais/mockup-geral.jpg'
REF=BASE/'MODEL_assets_v1/referencias/06-chat.png'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=Image.open(SOURCE).convert('RGB'); ref=Image.open(REF).convert('RGB')
panel_box=(1018,0,1174,404); panel=source.crop(panel_box)
assert ImageChops.difference(panel,ref).getbbox() is None
manifest={'schema':1,'source':{'path':str(SOURCE.relative_to(BASE)), 'sha256':sha(SOURCE),'size':list(source.size),'panel_global':panel_box,'panel_size':list(panel.size),'reference':str(REF.relative_to(BASE)),'reference_sha256':sha(REF),'panel_rgb_difference_bbox':None},'photos':[],'vectors':[]}
regions=[('avatar-header.png',(29,22,51,44),'circle',(11,11,10.2)),('avatar-received-first.png',(8,69,26,88),'circle',(9,9.5,8.05)),('avatar-received-last.png',(8,325,26,344),'circle',(9,9.5,8.05)),('campaign-office.png',(16,165,150,209),'top-rounded',(6,))]
for name,box,kind,params in regions:
    crop=panel.crop(box); w,h=crop.size; scale=16
    mask=Image.new('L',(w*scale,h*scale),0); d=ImageDraw.Draw(mask)
    if kind=='circle':
        cx,cy,r=params; d.ellipse(((cx-r)*scale,(cy-r)*scale,(cx+r)*scale-1,(cy+r)*scale-1),fill=255)
    else:
        r=params[0];d.rounded_rectangle((0,0,w*scale-1,h*scale-1),radius=r*scale,fill=255);d.rectangle((0,r*scale,w*scale-1,h*scale-1),fill=255)
    mask=mask.resize((w,h),Image.Resampling.LANCZOS)
    # Eliminate Lanczos ringing outside mathematical support, preserving only real photo pixels.
    for y in range(h):
        for x in range(w):
            if kind=='circle':
                cx,cy,r=params
                if math.hypot(x+.5-cx,y+.5-cy)>r+.5:mask.putpixel((x,y),0)
    rgba=crop.convert('RGBA');rgba.putalpha(mask)
    for y in range(h):
        for x in range(w):
            if mask.getpixel((x,y))==0:rgba.putpixel((x,y),(0,0,0,0))
    dest=OUT/name;rgba.save(dest)
    visible=opaque=0
    for y in range(h):
        for x in range(w):
            p=rgba.getpixel((x,y))
            if p[3]:
                visible+=1;assert p[:3]==crop.getpixel((x,y))
            if p[3]==255:opaque+=1
            if p[3]==0:assert p[:3]==(0,0,0)
    manifest['photos'].append({'file':name,'sha256':sha(dest),'size':[w,h],'local_box':box,'global_box':[box[0]+1018,box[1],box[2]+1018,box[3]],'alpha_geometry':kind,'geometry_parameters':params,'visible_pixels':visible,'opaque_pixels':opaque,'rgb_exact_all_nonzero_alpha':True,'hidden_rgb_zero':True,'classification':'source-photo-crop; geometry-only alpha; no UI text'})
a=panel.crop((8,69,26,88));b=panel.crop((8,325,26,344))
manifest['avatar_comparison']={'first_last_raw_rgb_equal':ImageChops.difference(a,b).getbbox() is None,'difference_bbox':ImageChops.difference(a,b).getbbox(),'decision':'Keep three independent crops. Same visual portrait identity; different JPEG RGB and header size. No exact duplicate or larger original proven.'}
vectors={
'back':('Voltar','<path d="m14 5-7 7 7 7"/>'),
'phone':('Telefone','<path d="M7 3 4 5c-2 4 5 13 10 15l3-1 2-3-4-3-2 2c-3-1-5-3-6-6l2-2Z"/>'),
'options':('Opções','<g fill="currentColor" stroke="none"><circle cx="12" cy="4" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="12" cy="20" r="1.4"/><circle cx="4" cy="12" r="1.4"/><circle cx="20" cy="12" r="1.4"/></g>'),
'location':('Localização','<path d="M18 10c0 5-6 10-6 10S6 15 6 10a6 6 0 1 1 12 0Z"/><circle cx="12" cy="10" r="2.2"/>'),
'calendar':('Duração','<rect x="4" y="6" width="16" height="15" rx="2"/><path d="M8 6V3m8 3V3M4 10h16m-12 5 3 3 5-6"/>'),
'money':('Cachê','<circle cx="12" cy="12" r="9"/><path d="m6 12 6-5 6 5v6H6Zm4 6v-5h4v5"/>'),
'paperclip':('Anexar','<path d="M9 17V7a3 3 0 0 1 6 0v11a5 5 0 0 1-10 0V7a7 7 0 0 1 14 0v10M9 8v10a1 1 0 0 0 2 0V8"/>'),
'send':('Enviar mensagem','<path d="m3 10 18-7-7 18-3-8Zm8 3L21 3"/>'),
'cellular':('Sinal celular simulado','<g fill="currentColor" stroke="none"><path d="M3 17h3v4H3zm5-4h3v8H8zm5-5h3v13h-3zm5-5h3v18h-3z"/></g>'),
'wifi':('Wi-Fi simulado','<path d="M3 8a15 15 0 0 1 18 0M6 12a10 10 0 0 1 12 0m-9 4a5 5 0 0 1 6 0"/><circle cx="12" cy="20" r=".7" fill="currentColor"/>'),
'battery':('Bateria simulada','<rect x="2" y="6" width="18" height="12" rx="2"/><path d="M22 10v4"/><rect x="4" y="8" width="14" height="8" rx=".5" fill="currentColor" stroke="none"/>')}
for name,(label,body) in vectors.items():
    path=OUT/(name+'.svg')
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round" role="img" aria-labelledby="title"><title id="title">{label}</title>{body}</svg>\n')
    manifest['vectors'].append({'file':path.name,'sha256':sha(path),'classification':'local-vector-approximation','accessible_title':label})
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'panel_rgb_equal':True,'photos':len(manifest['photos']),'vectors':len(vectors),'nonzero_alpha_rgb_exact':True,'hidden_rgb_zero':True,'avatars_raw_equal':manifest['avatar_comparison']['first_last_raw_rgb_equal']},ensure_ascii=False))
