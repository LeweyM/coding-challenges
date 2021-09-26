from unittest import TestCase

from src.linkedlists.llnode import build_linked_list
from src.linkedlists.removeduplicates import remove_duplicates


def get_removed_duplicates_list(values):
    return remove_duplicates(build_linked_list(values)).get_list()


class Test(TestCase):
    def test_remove_duplicates(self):
        self.assertEqual([5, 3], get_removed_duplicates_list([5, 3, 3]))
        self.assertEqual([0, 3, 1, 2, 4], get_removed_duplicates_list([0, 3, 1, 2, 3, 4, 4]))
        self.assertEqual([0], get_removed_duplicates_list([0, 0, 0, 0, 0]))
