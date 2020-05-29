# Author: LucasD11 <yuanzhendai@gmail.com>

from unittest import TestCase
from nameunity.lib.image_date import img_date


class TestImageDate(TestCase):
    def test_general_jpg(self):
        ts = img_date('tests/data/1.jpg')
        self.assertEqual(ts.year, 2020)
        self.assertEqual(ts.month, 5)
        self.assertEqual(ts.day, 3)
        self.assertEqual(ts.hour, 11)
        self.assertEqual(ts.minute, 33)
