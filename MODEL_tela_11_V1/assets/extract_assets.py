#!/usr/bin/env python3
"""Reproduce Tela11 assets using Pillow; run from any directory."""
from pathlib import Path
from PIL import Image, ImageChops
import hashlib,json,math
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
source=ROOT/'MODEL_assets_v1/originais/mockup-geral.jpg'
reference=ROOT/'MODEL_assets_v1/referencias/11-notificacoes.png'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
im=Image.open(source).convert('RGB');ref=Image.open(reference).convert('RGB')
frame=[805,434,989,751]
assert ImageChops.difference(im.crop(frame),ref).getbbox() is None
manifest={'source':{'path':str(source.relative_to(ROOT)),'sha256':sha(source),'size':list(im.size)},'reference':{'path':str(reference.relative_to(ROOT)),'sha256':sha(reference),'size':list(ref.size),'global_bbox':frame,'RGB_difference_bbox':None},'photos':[],'icons':[],'samples':{}}
# 28px support preserves full ~25–26px source disk and its genuine JPEG matte.
for n,y in [(1,75),(2,110),(3,145),(5,216),(6,251)]:
    box=[12,y,40,y+28];rgb=ref.crop(box);out=rgb.convert('RGBA');mask=Image.new('L',(28,28))
    for py in range(28):
        for px in range(28):
            mask.putpixel((px,py),255 if math.hypot(px-13.5,py-13.5)<=13.7 else 0)
    out.putalpha(mask)
    # Transparent RGB is cleared; all visible RGB remains exactly source.
    count=0
    for py in range(28):
        for px in range(28):
            if mask.getpixel((px,py)):
                assert out.getpixel((px,py))[:3]==rgb.getpixel((px,py));count+=1
            else:out.putpixel((px,py),(0,0,0,0))
    p=HERE/f'avatar-{n:02}.png';out.save(p)
    manifest['photos'].append({'file':p.name,'sha256':sha(p),'size':[28,28],'local_bbox':box,'global_bbox':[box[0]+805,box[1]+434,box[2]+805,box[3]+434],'circle_center_local':[25.5,y+13.5],'alpha':{'formula':'255 iff hypot(x-13.5,y-13.5)<=13.7 else 0','visible_pixels':count,'transparent_pixels':784-count,'transparent_RGB':[0,0,0],'partial_alpha':False},'visible_RGB_exact':True,'occluded_pixels':'None apparent inside photographic disk; source JPEG matte retained near edge. Detail beyond source unavailable.'})
icons={
'plus-circle':'<circle cx="12" cy="12" r="11" fill="#0c0c0c"/><path d="M12 6v12M6 12h12" stroke="#fff" stroke-width="1.4"/>',
'home':'<path d="m5 11 7-7 7 7v10h-5v-7h-4v7H5Z"/>',
'search':'<circle cx="10.5" cy="10.5" r="6.8"/><path d="m15.5 15.5 5 5"/>',
'plus':'<path d="M12 3v18M3 12h18"/>',
'chat':'<path d="M5 19 3 22l1-7C1 6 7 2 13 3c7 0 10 6 7 11-2 4-7 5-15 5Z"/>',
'profile':'<circle cx="12" cy="7" r="4" fill="#0c0c0c" stroke="none"/><path d="M4 22v-3a8 8 0 0 1 16 0v3Z" fill="#0c0c0c" stroke="none"/>',
'cellular':'<path d="M3 20v-3h3v3zm5 0v-7h3v7zm5 0V9h3v11zm5 0V4h3v16Z" fill="#111" stroke="none"/>',
'wifi':'<path d="M3 8a14 14 0 0 1 18 0M6 12a9 9 0 0 1 12 0M9 16a4 4 0 0 1 6 0" stroke="#111" stroke-width="2.4"/><circle cx="12" cy="19" r="1.4" fill="#111" stroke="none"/>',
'battery':'<rect x="1" y="6" width="19" height="12" rx="2" stroke="#111"/><rect x="3" y="8" width="15" height="8" rx="1" fill="#111" stroke="none"/><path d="M22 10v4" stroke="#111"/>',
'casting':'<circle cx="12" cy="12" r="12" fill="#bd6c4f" stroke="none"/><g stroke="#ead9c8" stroke-width=".65"><path d="M9 7.5v9m3-11v12m3-10v8M8 8h2m1-2h2m1 2h2M8 16h2m1 2h2m1-3h2"/></g>'}
for name,body in icons.items():
    p=HERE/f'{name}.svg'
    p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#94948f" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round">{body}</svg>\n')
    manifest['icons'].append({'file':p.name,'sha256':sha(p),'provenance':'New local vector approximation of Tela11 raster; no reused external artwork.','exact_raster_match':False})
for name,point in {'paper':[45,280],'inactive_pill':[145,52],'coral_left':[18,193],'coral_fill':[19,187],'black':[165,26]}.items():manifest['samples'][name]={'local_point':point,'RGB':list(ref.getpixel(tuple(point)))}
manifest['generator']={'file':'extract_assets.py','sha256':sha(Path(__file__)),'Pillow_version':__import__('PIL').__version__}
(HERE/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Verified: reference RGB exact; five RGBA frames visible RGB exact; generated 10 SVGs.')
