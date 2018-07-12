from lru_cache.lru_based_on_stack import LRUCacheBasedOnStack


class cache():
    def __init__(self, function):
        self.function = function
        self.lru_cache = LRUCacheBasedOnStack(length=3)

    def __call__(self, *args):
        item = '{}-{}-{}'.format(*args)
        if not self.lru_cache.if_in_lru_item_list(item):
            self.function(*args)
            self.lru_cache.insert_item(item)
        return item