"""Copy raw Playwright screenshots to the canonical delivery names; no image edits."""
from pathlib import Path
import hashlib
import shutil
ROOT=Path(__file__).resolve().parent
for width,height in [(375,812),(390,844),(430,932)]:
    source=ROOT/'screenshots'/f'{width}x{height}.png'
    target=ROOT/f'captura-{width}.png'
    shutil.copyfile(source,target)
    assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest()
print('Three raw screenshot aliases exported byte-for-byte.')
