from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[2]
a=Image.open(root/'MODEL_assets_v1/referencias/01-splash.png').convert('RGB').crop((1,18,187,249))
b=Image.open(root/'MODEL_tela_01_V1/assets/retrato.png').convert('RGB')
assert a.tobytes()==b.tobytes(), 'Hero não corresponde ao recorte original'
print('01 hero RGB: idêntico ao recorte original')
src=Image.open(root/'MODEL_assets_v1/referencias/02-descoberta.png').convert('RGBA')
for name,box in [('enzo',(6,89,112,244)),('gabriel',(116,89,194,199)),('theo',(6,248,112,364)),('rafael',(116,202,194,364))]:
 a=src.crop(box);b=Image.open(root/f'MODEL_tela_02_V1/assets/{name}.png').convert('RGBA')
 mismatch=sum(1 for p,q in zip(a.getdata(),b.getdata()) if q[3] and p!=q)
 assert mismatch==0, f'{name}: {mismatch} pixels divergentes fora das máscaras'
 print(f'{name}: 0 pixels divergentes fora das máscaras')
