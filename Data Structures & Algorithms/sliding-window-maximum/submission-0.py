class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        left, right = 0, k

        listElem = nums[left:right]
        listMax = []

        while right <= len(nums):
            listMax.append(max(listElem))
            if right == len(nums):
                break
            listElem.pop(0)
            listElem.append(nums[right])
            left += 1
            right += 1
        
        return listMax