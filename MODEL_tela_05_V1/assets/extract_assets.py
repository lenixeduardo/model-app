#!/usr/bin/env python3
"""Reproduce panel05 crops without resampling, RGB edits or generated photography."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageChops
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SRC=ROOT/'MODEL_assets_v1/originais/mockup-geral.jpg'
REF=ROOT/'MODEL_assets_v1/referencias/05-portfolio.png'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
im=Image.open(SRC).convert('RGB'); panel=im.crop((836,0,1008,404))
assert panel.tobytes()==Image.open(REF).convert('RGB').tobytes()
items=[('foto-01-camisa-aberta.png',(3,77,109,256),False,'Camisa branca aberta, rosto inclinado'),('foto-02-torso-interior.png',(111,77,169,163),False,'Torso frontal, interior quente'),('foto-03-perfil-praia.png',(111,165,169,246),False,'Perfil e torso, mar ao fundo'),('foto-04-monocromatica.png',(3,258,109,359),False,'Retrato monocromático com braço à frente'),('foto-05-camiseta-branca.png',(111,247,169,327),False,'Camiseta branca e colar'),('foto-06-rosto-parcial-inferior.png',(3,360,109,404),True,'Rosto e cabelo, olhar lateral; parcial inferior'),('foto-07-sentado-parcial-inferior.png',(111,329,169,404),True,'Sentado, roupa preta sem mangas; parcial inferior')]
outer=Image.new('L',(172,404));ImageDraw.Draw(outer).rounded_rectangle((0,-10,171,403),radius=10,fill=255)
photos={}
for name,box,partial,desc in items:
 x1,y1,x2,y2=box; w,h=x2-x1,y2-y1
 rgb=panel.crop(box); mask=Image.new('L',(w,h));d=ImageDraw.Draw(mask)
 # Partial tiles extend below viewport; their bottom corners must not be rounded as if complete.
 d.rounded_rectangle((0,0,w-1,h+10 if partial else h-1),radius=3,fill=255)
 mask=ImageChops.multiply(mask,outer.crop(box))
 rgba=rgb.convert('RGBA');rgba.putalpha(mask);p=OUT/name;rgba.save(p)
 assert rgba.convert('RGB').tobytes()==rgb.tobytes()
 photos[name]={'description':desc,'partialInferior':partial,'cropPanelLocalLTRBExclusive':box,'cropGlobalLTRBExclusive':[x1+836,y1,x2+836,y2],'size':[w,h],'aspectRatio':w/h,'sha256':sha(p),'opaquePixels':mask.histogram()[255],'transparentPixels':mask.histogram()[0],'alpha':'Binary rounded tile radius3; partials extended below viewport, intersect panel radius10. RGB untouched including transparent pixels.'}
icons={
 'busca.svg':'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.2 15.2 4.5 4.5"/></svg>\n',
 'status-sinais.svg':'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34 10" fill="currentColor"><path d="M0 8h2V6H0zm3 0h2V4H3zm3 0h2V2H6zm3 0h2V0H9z"/><g fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"><path d="M14 3q4-4 8 0M16 5q2-2 4 0"/><rect x="25" y="2" width="7" height="4" rx="1"/></g><circle cx="18" cy="7" r=".8"/><path d="M26 3h5v2h-5zM33 3h1v2h-1z"/></svg>\n'}
(OUT/'icons').mkdir(exist_ok=True)
for name,s in icons.items():(OUT/'icons'/name).write_text(s)
shutil.copyfile(ROOT/'MODEL_tela_04_V1/assets/icons/voltar.svg',OUT/'icons/voltar.svg')
manifest={'source':str(SRC.relative_to(ROOT)),'sourceSha256':sha(SRC),'reference':str(REF.relative_to(ROOT)),'referenceSha256':sha(REF),'referencePanelGlobalLTRBExclusive':[836,0,1008,404],'referenceRGBExact':True,'operation':'Original JPEG decoded to RGB; crops exported losslessly as RGBA PNG. Only alpha boundary masking. No RGB changes, resampling, synthesis, restoration or UI labels.','photos':photos,'icons':{name:{'sha256':sha(OUT/'icons'/name),'source':'MODEL_tela_04_V1/assets/icons/voltar.svg (byte-identical)' if name=='voltar.svg' else 'Manual SVG approximation of panel05; original vectors unavailable'} for name in ['voltar.svg',*icons]},'scriptSha256':sha(Path(__file__))}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Verified 7 RGB-exact crops, 3 SVGs; manifest written.')
