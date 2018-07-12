from unittest import TestCase
from lru_cache.lru_based_on_stack import LRUCacheBasedOnStack


class TestLRUCacheBasedOnStack(TestCase):
    def setUp(self):
        self.item_zero = '0-0-0'
        self.item_one = '1-1-1'
        self.item_two = '2-2-2'
        self.item_there = '3-3-3'
        self.item_four = '4-4-4'
        self.cache = LRUCacheBasedOnStack(2)

    def return_lru_cache_list(self):
        return self.cache.lru_item_list

    def test_if_in_lru_item_list(self):
        # Add elements to lru cache
        self.cache.insert_item(self.item_one)
        self.cache.insert_item(self.item_there)
        self.cache.insert_item(self.item_two)

        self.assertEqual(self.cache.if_in_lru_item_list(self.item_there), True)
        self.assertEqual(self.cache.if_in_lru_item_list(self.item_four), False)

    def test_insert_item(self):
        # Add first element which doesn’t exist in cache
        self.cache.insert_item(self.item_zero)
        self.assertEqual(self.return_lru_cache_list(),
                         [self.item_zero])
        # Add second element which doesn’t exist in cache
        self.cache.insert_item(self.item_one)
        self.assertEqual(self.return_lru_cache_list(),
                         [self.item_one, self.item_zero])
        # Add next element which doesn’t exist in cache
        self.cache.insert_item(self.item_two)
        self.assertEqual(self.return_lru_cache_list(),
                         [self.item_two, self.item_one, self.item_zero])
        # Add next element which doesn’t exist in cache, and causes overflow of the list
        self.cache.insert_item(self.item_there)
        self.assertEqual(self.return_lru_cache_list(),
                         [self.item_there, self.item_two, self.item_one])
        # Add element which exist in cache
        self.cache.insert_item(self.item_two)
        self.assertEqual(self.return_lru_cache_list(),
                         [self.item_two, self.item_there, self.item_one])

    def test_remove_item(self):
        # Add elements to lru cache
        self.cache.insert_item(self.item_one)
        self.cache.insert_item(self.item_there)
        self.cache.insert_item(self.item_two)
        self.assertEqual(self.return_lru_cache_list(),
                         [self.item_two, self.item_there, self.item_one])
        # Remove element from lru cache
        self.cache.remove_item(self.item_there)
        self.assertEqual(self.return_lru_cache_list(), [self.item_two, self.item_one])
