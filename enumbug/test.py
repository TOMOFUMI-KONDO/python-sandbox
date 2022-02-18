import unittest

from enumbug.b import B
from enumbug.enums import Color


class Test(unittest.TestCase):
    def test(self):
        b = B()
        self.assertEqual(b.color, Color.RED)
