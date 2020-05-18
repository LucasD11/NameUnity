# Author: LucasD11 <yuanzhendai@gmail.com>

from unittest import TestCase
from nameunity import formatters


class TestFormatter1(TestCase):
    def test_valid_filename(self):
        filename = "IMG_20010201_120030.jpg"
        date = formatters.Formatter1().format(filename)
        self.assertEqual(date.year, 2001)
        self.assertEqual(date.month, 2)
        self.assertEqual(date.day, 1)
        self.assertEqual(date.hour, 12)
        self.assertEqual(date.minute, 0)
        self.assertEqual(date.second, 30)

    def test_invalid_filename(self):
        filename = "invalid"
        with self.assertRaises(formatters.UnknownFormat):
            formatters.Formatter1().format(filename)

    def test_real_filename(self):
        formatters.Formatter1().format("IMG_20180310_105814.jpg")
