from unittest import TestCase

from src.strings.removeduplicates import remove_duplicates


class Test(TestCase):
    def test_is_anagram(self):
        self.assertEqual("helo", remove_duplicates("hello"))
        self.assertEqual("godbye", remove_duplicates("goodbye"))
