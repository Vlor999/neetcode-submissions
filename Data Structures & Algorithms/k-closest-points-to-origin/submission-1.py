class Solution:
    def getDistance2(self, position: list[int]) -> int:
        return position[0] ** 2 + position[1] ** 2

    def getPosition(self, priorityQueueVal: list[int], val: int) -> int:
        left, right = 0, len(priorityQueueVal)
        while left < right:
            mid = (left + right) // 2
            if priorityQueueVal[mid] < val:
                left = mid + 1
            else:
                right = mid
        return left

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        priorityQueue = []
        priorityQueueDistance = []
        for point in points:
            distance = self.getDistance2(point)
            posInsertion = self.getPosition(priorityQueueDistance, distance)
            if len(priorityQueue) < k:
                priorityQueue.insert(posInsertion, point)
                priorityQueueDistance.insert(posInsertion, distance)
            else:
                if distance < priorityQueueDistance[-1]:
                    priorityQueue.insert(posInsertion, point)
                    priorityQueueDistance.insert(posInsertion, distance)
                    priorityQueue.pop()
                    priorityQueueDistance.pop()
        return priorityQueue