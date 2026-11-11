from pathlib import Path
import json
p=Path(__file__).parent
m=json.loads((p/'assets/manifest.json').read_text())
assert len(m['photos'])==5 and len(m['icons'])==10
assert all(x['visible_RGB_exact'] for x in m['photos'])
assert not (p/'index.html').exists(), 'Initial gate must run before implementation'
print('PASS: initial asset contract; no HTML before implementation')
