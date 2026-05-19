#! /usr/bin/env python3

class PrefixTree:

    def __init__(self):
        self.listElem = []

    def insert(self, word: str) -> None:
        left, right = 0, len(self.listElem) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.listElem[mid] < word:
                left = mid + 1
            elif self.listElem[mid] > word:
                right = mid - 1
            else:
                return  # The value is already present
        self.listElem.insert(left, word)
        
    def search(self, word: str) -> bool:
        left, right = 0, len(self.listElem) - 1
        if left > right:
            return False
        while left < right:
            mid = (left + right) // 2
            if self.listElem[mid] < word:
                left = mid + 1
            elif self.listElem[mid] > word:
                right = mid - 1
            else:
                return True
        return self.listElem[left] == word

    def startsWith(self, prefix: str) -> bool:
        left, right = 0, len(self.listElem) - 1
        if left > right:
            return False
        while left < right:
            mid = (left + right) // 2
            if self.listElem[mid] < prefix:
                left = mid + 1
            elif self.listElem[mid] > prefix:
                right = mid - 1
            else:
                return True
        return self.listElem[left][:len(prefix)] == prefix