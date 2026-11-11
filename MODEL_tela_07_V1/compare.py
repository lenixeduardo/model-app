from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
r=Path(__file__).resolve().parent
ref=Image.open(r.parent/'MODEL_assets_v1/referencias/07-castings.png').convert('RGB');shot=Image.open(r/'captura-390.png').convert('RGB')
ref=ref.resize((round(ref.width*844/ref.height),844),Image.Resampling.NEAREST)
canvas=Image.new('RGB',(ref.width+390+24,874),'#dedcd6');canvas.paste(ref,(0,30));canvas.paste(shot,(ref.width+24,30));d=ImageDraw.Draw(canvas);d.text((8,8),'Fonte 201x317 ampliada proporcionalmente',fill='black');d.text((ref.width+30,8),'Candidato 390x844 raw',fill='black');canvas.save(r/'comparacao-390.png')
