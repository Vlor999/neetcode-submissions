class Solution:
    def foundPositionInsertion(self, priorityQueue: list[int], num: int) -> int:
        left:int = 0
        right:int = len(priorityQueue)
        while left < right:
            mid: int = (left + right) // 2
            if priorityQueue[mid] < num:
                right = mid
            else:
                left = mid + 1
        return left

    def findKthLargest(self, nums: list[int], k: int) -> int:
        priorityQueue: list[int] = []
        for num in nums:
            foundPosition:int = self.foundPositionInsertion(priorityQueue, num)
            priorityQueue.insert(foundPosition, num)
            if len(priorityQueue) > k:
                priorityQueue.pop()
        return priorityQueue[-1]