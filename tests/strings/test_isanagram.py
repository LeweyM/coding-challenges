from unittest import TestCase

from src.strings.isanagram import is_anagram


class Test(TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("cat", "tac"))
        self.assertTrue(is_anagram("abcde", "cedab"))
        self.assertFalse(is_anagram("cat", "tzc"))
        self.assertFalse(is_anagram("aa", "bb"))
        self.assertFalse(is_anagram("CAT", "cat"))
