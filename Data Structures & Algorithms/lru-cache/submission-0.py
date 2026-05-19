from collections import deque 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = {}
        self.queue = deque()
        

    def get(self, key: int) -> int:
        val = self.LRU.get(key, -1)
        if val != -1:
            self.queue.remove(key)
            self.queue.append(key)
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.queue.remove(key)
        elif len(self.LRU) == self.capacity:
            del self.LRU[self.queue.popleft()]
        self.LRU[key] = value
        self.queue.append(key)
        