class MedianFinder:

    def __init__(self):
        self.taille:int = 0
        self.streamElement: list[int] = []

    def foundPosition(self, num:int) -> int:
        left:int = 0
        right:int = len(self.streamElement)
        while left < right:
            mid:int  = (left + right) // 2
            if self.streamElement[mid] > num:
                left = mid + 1
            else :
                right = mid
        return left

    def addNum(self, num: int) -> None:
        self.taille += 1
        pos:int = self.foundPosition(num)
        self.streamElement.insert(pos, num)

    def findMedian(self) -> float:
        if self.taille % 2 == 1:
            return self.streamElement[self.taille // 2]
        else:
            return (self.streamElement[self.taille // 2] + self.streamElement[-1 + self.taille // 2]) / 2
        