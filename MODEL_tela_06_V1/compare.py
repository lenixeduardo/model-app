from PIL import Image,ImageDraw
from pathlib import Path
R=Path(__file__).resolve().parent
ref=Image.open(R.parent/'MODEL_assets_v1/referencias/06-chat.png').convert('RGB');shot=Image.open(R/'screenshots/390x844.png').convert('RGB');ref=ref.resize((round(ref.width*844/ref.height),844),Image.Resampling.LANCZOS)
canvas=Image.new('RGB',(ref.width+shot.width+24,884),'#deded8');canvas.paste(ref,(0,40));canvas.paste(shot,(ref.width+24,40));d=ImageDraw.Draw(canvas);d.text((8,12),'Referencia156x404 proporcional H844',fill='black');d.text((ref.width+28,12),'Chromium390x844 DPR1',fill='black');canvas.save(R/'comparacao-390.png')
