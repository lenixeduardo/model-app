from pathlib import Path
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent
ref=Image.open(r.parent/'MODEL_assets_v1/referencias/05-portfolio.png').convert('RGB');shot=Image.open(r/'captura-390.png').convert('RGB')
a=ref.resize((round(ref.width*844/ref.height),844),Image.Resampling.LANCZOS);b=shot
out=Image.new('RGB',(a.width+b.width+16,874),'#deddd8');out.paste(a,(0,30));out.paste(b,(a.width+16,30));d=ImageDraw.Draw(out);d.text((8,8),'Referencia05 | altura844 proporcional',fill='black');d.text((a.width+24,8),'Chromium390x844',fill='black');out.save(r/'comparacao-390.png')
