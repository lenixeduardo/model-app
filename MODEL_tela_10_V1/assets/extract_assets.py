from pathlib import Path
from PIL import Image, ImageChops
import hashlib,json,math,shutil
P=Path(__file__).resolve().parent; ROOT=P.parent.parent
src=ROOT/'MODEL_assets_v1/referencias/10-meu-perfil.png'; orig=ROOT/'MODEL_assets_v1/originais/mockup-geral.jpg'
ref=Image.open(src).convert('RGB'); global_im=Image.open(orig).convert('RGB')
assert ImageChops.difference(ref,global_im.crop((612,434,797,751))).getbbox() is None
box=(53,39,130,116); crop=ref.crop(box); rgba=crop.convert('RGBA'); n=0; holes=0
for y in range(77):
 for x in range(77):
  # Binary alpha preserves the RGB of every surviving JPEG pixel exactly.
  outer=math.hypot(x+.5-38.5,y+.5-38.5)<=38.5
  hole=math.hypot(x+.5-64.5,y+.5-64)<=12.5
  if not outer or hole: rgba.putpixel((x,y),(0,0,0,0)); holes+=int(outer and hole)
  else: assert rgba.getpixel((x,y))[:3]==crop.getpixel((x,y)); n+=1
rgba.save(P/'matheus-avatar.png')
def svg(name,body,fill='none',stroke='currentColor',width='1.55',vb='0 0 24 24'):
 (P/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round">{body}</svg>\n')
reuse={}
for name in ['cellular','wifi','battery','search','chat','plus','location']:
 old=ROOT/'MODEL_tela_07_V1/assets'/f'{name}.svg'; shutil.copyfile(old,P/old.name); reuse[old.name]={'source':str(old.relative_to(ROOT)),'sha256':hashlib.sha256(old.read_bytes()).hexdigest()}
svg('back','<path d="m14 5-7 7 7 7"/>')
svg('chevron','<path d="m9 5 7 7-7 7"/>')
svg('nav-home','<path d="m3 10 9-8 9 8v12h-6v-8H9v8H3Z"/>')
svg('profile-active','<circle cx="12" cy="7" r="4"/><path d="M4 22v-2a8 6 0 0 1 16 0v2Z"/>',fill='#111111',stroke='none')
svg('verified','<path fill="#111" stroke="none" d="m12 1 3 2 3.5.5 1 3.5 2 3-1 3.5-.5 3.5-3.5 1-3 2-3.5-1-3.5-.5-1-3.5-2-3 1-3.5.5-3.5 3.5-1Z"/><path stroke="#fff" stroke-width="2" d="m7 11 3 3 7-7"/>')
svg('portfolio','<rect x="4" y="5" width="16" height="17" rx="2"/><path d="M8 2v6m8-6v6M4 10h16m-11 4h6m-6 4h4"/>')
svg('availability','<rect x="4" y="5" width="16" height="17" rx="3"/><path d="M8 2v5m8-5v5m-4 4v5l3 2"/>')
svg('fee','<rect x="3" y="8" width="18" height="13" rx="2"/><path d="M8 8V4h8v4M3 13h18m-11 0v3h4v-3"/>')
svg('statistics','<path d="M3 22V12h4v10m3 0V3h4v19m3 0V8h4v14M2 22h20"/>')
svg('plans','<circle cx="12" cy="6" r="4"/><path d="M4 22v-3a8 7 0 0 1 16 0v3Zm4-7 4 4 4-4"/>')
# Co-registered 77-square overlay. Opaque support exceeds alpha hole by 1px.
svg('edit-overlay','<circle cx="64.5" cy="64" r="13.5" fill="#f8f7f3" stroke="none"/><g stroke="#191919" stroke-width="1.7"><path d="M61 60h-3v11h11v-4m-8-1 9-9 3 3-9 9-4 1Z"/><path d="m68 59 3 3"/></g>',vb='0 0 77 77')
# Same opaque support for standalone control; use overlay for exact registration.
svg('edit','<circle cx="12" cy="12" r="12" fill="#f8f7f3" stroke="none"/><g stroke="#191919"><path d="M9 8H6v11h11v-4m-8-1 9-9 3 3-9 9-4 1Z"/><path d="m16 7 3 3"/></g>')
hashfile=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={p.name:{'sha256':hashfile(p),'bytes':p.stat().st_size} for p in sorted(P.iterdir()) if p.suffix in ['.svg','.png','.py']}
manifest={'source':{'reference':str(src.relative_to(ROOT)),'sha256':hashfile(src),'size':[185,317],'original':str(orig.relative_to(ROOT)),'original_sha256':hashfile(orig),'global_crop':[612,434,797,751],'crop_rgb_equal':True},'avatar':{'file':'matheus-avatar.png','identity':'Matheus Silva, 24 — exclusively screen10','local_box':list(box),'global_box':[665,473,742,550],'size':[77,77],'ratio':1,'circle_center_crop':[38.5,38.5],'circle_radius':38.5,'alpha':'binary geometric; outside circle and edit footprint transparent RGB=0','edit_hole_center_crop':[64.5,64],'edit_hole_radius':12.5,'edit_overlay':'edit-overlay.svg','support_radius':13.5,'visible_rgb_exact':True,'visible_pixels':n,'ui_hole_pixels':holes,'no_inpainting':True},'palette':{'paper':'#f8f7f3','chips':'#efeeea','primary':'#111111','secondary_approx':'#70706c'},'reuse':reuse,'files':files,'limits':['77px JPEG photo; enlargement does not restore detail','SVGs approximated from screen10; reused vectors checked for role','Binary circle edge retains JPEG matte at circumference; no RGB recoloring','Keep image width fluid and height auto; overlay absolute inset 0 width/height 100%; permanent opaque support','Do not apply object-fit cover, independent overlay scaling or remove support in dialogs; 44px hit target can be transparent around visible support']}
(P/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'visible_rgb_exact':True,'pixels':n,'hole':holes,'files':len(files)}))
