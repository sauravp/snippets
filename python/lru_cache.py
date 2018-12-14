# https://www.interviewbit.com/problems/lru-cache

from collections import OrderedDict

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.keys = []
        

    # @return an integer
    def get(self, key):
        if key in self.keys:
            result = self.cache[key]
            del self.cache[key]
            self.cache[key] = result
            return result
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.keys:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            item = self.cache.popitem(last=False)
            self.keys.remove(item[0])
            self.keys.append(key)
        else:
            self.keys.append(key)
        self.cache[key] = value
