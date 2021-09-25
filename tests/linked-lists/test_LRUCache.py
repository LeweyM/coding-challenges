from unittest import TestCase

from src.LRUCache import LRUCache


class TestLRUCache(TestCase):
    def test_lru_cache_1(self):
        cache = LRUCache(2)
        cache.set(5, 0)
        cache.set(6, 1)
        self.assertEqual(1, cache.get(6))
        self.assertEqual(0, cache.get(5))

        cache.set(7, 2)
        self.assertEqual(-1, cache.get(6))
        self.assertEqual(0, cache.get(5))
        self.assertEqual(2, cache.get(7))

    def test_lru_cache_2(self):
        cache = LRUCache(5)
        cache.set(0, 50)
        cache.set(1, 51)
        cache.set(2, 52)
        cache.set(3, 53)
        cache.set(4, 54)
        # hits cap here. Last set was "0"
        cache.set(5, 55)
        self.assertEqual(-1, cache.get(0))
        self.assertEqual(55, cache.get(5))

        # after getting "1", "2" is the least recently used
        self.assertEqual(51, cache.get(1))
        cache.set(6, 56)
        self.assertEqual(-1, cache.get(2))


