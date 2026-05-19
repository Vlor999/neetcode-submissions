class Solution:
    def foundPos(self, orderedQueue: list[int], val: int) -> int:
        left, right = 0, len(orderedQueue)
        while left < right:
            mid = (left + right) // 2
            if orderedQueue[mid] < val:
                left = mid + 1
            else:
                right = mid
        return left

    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        else:
            orderedStones = sorted(stones)
            while len(orderedStones) > 1:
                x, y = orderedStones.pop(), orderedStones.pop()
                if x < y or x > y:
                    pos = self.foundPos(orderedStones, abs(y-x))
                    orderedStones.insert(pos, abs(y - x))
            return orderedStones[0] if len(orderedStones) > 0 else 0