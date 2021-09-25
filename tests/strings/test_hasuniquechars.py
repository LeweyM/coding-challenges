from unittest import TestCase

from src.strings.hasuniquechars import has_unique_chars


class Test(TestCase):
    def test_has_unique_chars(self):
        self.assertTrue(has_unique_chars("abc"))
        self.assertFalse(has_unique_chars("abca"))
        self.assertFalse(has_unique_chars("aab"))
        self.assertTrue(has_unique_chars(""))
