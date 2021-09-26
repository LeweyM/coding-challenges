from unittest import TestCase

from src.linkedlists.llnode import build_linked_list
from src.linkedlists.partition import partition


class Test(TestCase):
    def test_partition(self):
        res = partition(build_linked_list([1, 6, 2, 7, 3, 8]), 5).get_list()
        self.assertEqual([1, 3, 2, 7, 6, 8], res)
