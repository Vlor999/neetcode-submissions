class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.listElem = sorted(nums, reverse=True)
        self.listElem = self.listElem[:k]
        self.pos = k
        self.best = self.listElem[-1] if len(nums) > 0 else None

    def binaryInsertion(self, val: int):
        left, right = 0, len(self.listElem)
        while left < right:
            mid = (left + right) // 2
            if self.listElem[mid] > val:
                left = mid + 1
            else:
                right = mid
        self.listElem.insert(left, val)

    def add(self, val: int) -> int:
        if self.best != None and val <= self.best:
            return self.best
        else:
            self.binaryInsertion(val)
            if len(self.listElem) > self.pos:
                self.listElem.pop()
            self.best = self.listElem[-1]
            return self.best
