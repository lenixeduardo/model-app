from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parent
ref=Image.open(root.parent/'MODEL_assets_v1/referencias/04-perfil-modelo.png').convert('RGB');shot=Image.open(root/'captura-390.png').convert('RGB')
def normalize(im):return im.resize((round(im.width*844/im.height),844),Image.Resampling.LANCZOS)
a,b=normalize(ref),normalize(shot);canvas=Image.new('RGB',(a.width+b.width+16,874),'#deddd8');canvas.paste(a,(0,30));canvas.paste(b,(a.width+16,30));d=ImageDraw.Draw(canvas);d.text((8,8),'Referencia 04 | altura 844, proporcao preservada',fill='black');d.text((a.width+24,8),'Chromium 390 x 844',fill='black');canvas.save(root/'comparacao-390.png')
