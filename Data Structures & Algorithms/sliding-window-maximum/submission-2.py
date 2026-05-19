class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:        
        left, right = 0, k
        elemMax = max(nums[left:right])
        indice = left + nums[left:right].index(elemMax)
        listMax = [elemMax]
        while right < len(nums):
            left += 1
            right += 1
            if indice < left:
                elemMax = max(nums[left:right])
                indice = left + nums[left:right].index(elemMax)
            else:
                if nums[right - 1] >= elemMax:
                    elemMax = nums[right - 1]
                    indice = right - 1
            listMax.append(elemMax)
        return listMax