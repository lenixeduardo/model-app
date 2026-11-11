from pathlib import Path
import unittest
class Contract(unittest.TestCase):
 def test_native_entry_exists(self):
  p=Path(__file__).resolve().parents[1]/'index.html'
  self.assertTrue(p.exists(),'native HTML entry missing')
if __name__=='__main__': unittest.main()
