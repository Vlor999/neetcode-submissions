class Solution:
    def canEat(self, piles: list[int], speed: int, h: int) -> bool:
        currentTemps = 0
        for banana in piles:
            currentTemps += (banana + speed - 1) // speed
        return currentTemps <= h

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        minVitesse, maxVitesse = 1, max(piles)
        while minVitesse < maxVitesse:
            mid = (minVitesse + maxVitesse) // 2
            if self.canEat(piles, mid, h):
                maxVitesse = mid
            else:
                minVitesse = mid + 1
        return minVitesse