class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            count = 0
            for pile in piles:
                nb_it =  math.ceil(pile / mid)
                count += nb_it
            if count > h:
                left = mid + 1
            else:
                right = mid
        return left