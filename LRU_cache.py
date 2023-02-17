class LRUCache:
    def __init__(self, capacity):
        self.hashmap = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.hashmap:
            return -1
        v = self.hashmap.pop(key) 
        self.hashmap[key] = v
        return v

    def put(self, key, value):
        if key in self.hashmap:    
            self.hashmap.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:
                self.hashmap.popitem(last=False) 
        self.hashmap[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)