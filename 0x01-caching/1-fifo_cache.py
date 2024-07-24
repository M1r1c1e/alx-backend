#!/usr/bin/env python3
"""A caching system.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism.
    """
    def __init__(self):
        """Initializing the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adding an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """taking an item by key.
        """
        return self.cache_data.get(key, None)
