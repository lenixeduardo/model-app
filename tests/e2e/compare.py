from PIL import Image, ImageDraw
from pathlib import Path
root=Path(__file__).resolve().parents[2]
out=root/'docs/correcoes-123/capturas'
for n,name in [('01','splash'),('02','descoberta')]:
 for w,h in [(375,812),(390,844),(430,932)]:
  ref=Image.open(root/f'MODEL_assets_v1/referencias/{n}-{name}.png').convert('RGB')
  ref=ref.resize((w,round(ref.height*w/ref.width)),Image.Resampling.LANCZOS)
  actual=Image.open(out/f'{n}-{w}.png').convert('RGB')
  result=Image.new('RGB',(2*w,max(h,ref.height)),(65,65,65));result.paste(ref,(0,0));result.paste(actual,(w,0))
  result.save(out/f'{n}-comparacao-{w}.png')
