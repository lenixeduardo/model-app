from PIL import Image, ImageDraw
from pathlib import Path
root=Path(__file__).resolve().parent.parent
src=root/'MODEL_assets_v1/referencias'
# Partial hero preserves supplied photograph, original wordmark and divider.
a=Image.open(src/'01-splash.png').convert('RGB')
a.crop((1,18,187,249)).save(root/'MODEL_tela_01_V1/assets/retrato.png')
# Only small source UI areas are made transparent. Other pixels remain intact.
a=Image.open(src/'02-descoberta.png').convert('RGBA')
crops=[('enzo',(6,89,112,244),[(12,211,70,222),(12,226,67,236),(94,220,105,235)]),('gabriel',(116,89,194,199),[(120,168,170,179),(120,182,187,192)]),('theo',(6,248,112,364),[(12,334,55,344),(12,347,84,358)]),('rafael',(116,202,194,364),[(120,334,170,344),(120,347,174,358),(176,341,189,357)])]
for name,box,masks in crops:
 im=a.crop(box); draw=ImageDraw.Draw(im)
 for x1,y1,x2,y2 in masks: draw.rectangle((x1-box[0],y1-box[1],x2-box[0]-1,y2-box[1]-1),fill=(0,0,0,0))
 im.save(root/f'MODEL_tela_02_V1/assets/{name}.png')
