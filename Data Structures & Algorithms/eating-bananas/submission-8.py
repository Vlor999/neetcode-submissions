import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)
        
        while mini < maxi:
            mid = (mini + maxi) // 2
            hours_spent = sum(math.ceil(pile / mid) for pile in piles)
            if hours_spent <= h:
                maxi = mid
            else:
                mini = mid + 1
        return mini