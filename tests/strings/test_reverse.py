from unittest import TestCase

from src.strings.reverse import reverse


class Test(TestCase):
    def test_is_anagram(self):
        self.assertEqual("cba", reverse("abc"))
        self.assertEqual("aa", reverse("aa"))
