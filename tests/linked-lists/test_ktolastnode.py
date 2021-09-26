from unittest import TestCase

from src.linkedlists.ktolastnode import k_to_last_node
from src.linkedlists.llnode import build_linked_list


class Test(TestCase):
    def test_k_to_last_node(self):
        self.assertEqual(4, k_to_last_node(build_linked_list([1, 2, 3, 4, 5]), 1).value)
        self.assertEqual(5, k_to_last_node(build_linked_list([1, 2, 3, 4, 5]), 0).value)
        self.assertEqual(2, k_to_last_node(build_linked_list([1, 2, 3, 4, 5]), 3).value)
        self.assertEqual("ILLEGAL", k_to_last_node(build_linked_list([1, 2, 3, 4, 5]), 5))

