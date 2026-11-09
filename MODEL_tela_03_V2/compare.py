#!/usr/bin/env python3
"""Normalize reference/capture height without changing either aspect ratio."""
from pathlib import Path
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parent
reference = Image.open(ROOT.parent/'MODEL_assets_v1/referencias/referencia-tela-03.png').convert('RGB')
capture = Image.open(ROOT/'captura-390.png').convert('RGB')
height = capture.height
reference = reference.resize((round(reference.width*height/reference.height),height),Image.Resampling.LANCZOS)
canvas = Image.new('RGB',(reference.width+capture.width+54,height+52),'#e7e2d9')
draw = ImageDraw.Draw(canvas)
draw.text((12,12),'REFERENCIA (proporcao preservada)',fill='#151515')
draw.text((reference.width+36,12),'V2 REAL - CHROMIUM - 390 x 844',fill='#151515')
canvas.paste(reference,(12,40)); canvas.paste(capture,(reference.width+36,40))
canvas.save(ROOT/'comparacao-390.png')
print(ROOT/'comparacao-390.png')
