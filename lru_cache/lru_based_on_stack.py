class LRUCacheBasedOnStack(object):
    """ Implements LRU based on stack """

    def __init__(self, length):
        self.lru_length = length
        self.lru_item_list = list()

    def if_in_lru_item_list(self, item):
        """ Check if item exist in lru cache """

        return True if item in self.lru_item_list else False

    def insert_item(self, item):
        """ Add to lru cache """

        if self.if_in_lru_item_list(item):
            # Item exist - move to index 0
            self.remove_item(item)
            self.lru_item_list.insert(0, item)
        else:
            # Item does not exist
            if len(self.lru_item_list) > self.lru_length:
                # New item causes overflow of the list
                self.remove_item(self.lru_item_list[-1])
            self.lru_item_list.insert(0, item)

    def remove_item(self, item):
        """ Remove item """

        del self.lru_item_list[self.lru_item_list.index(item)]






