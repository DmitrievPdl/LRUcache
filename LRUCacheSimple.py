from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()

    def get(self, key: str) -> int:
        if key in self.map:
            value = self.map.pop(key)
            self.map[key] = value
            return value
        return ''
    
    def set(self, key: str, value: str) -> None:
        if key in self.map:
            self.map.pop(key)
        elif len(self.map) == self.capacity:
            self.map.popitem(last=False)
        self.map[key] = value

    def delete(self, key: str) -> None:
        if key in self.map:
            self.map.pop(key)