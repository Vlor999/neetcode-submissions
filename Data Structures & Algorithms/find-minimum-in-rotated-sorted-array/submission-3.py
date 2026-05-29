class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid
            elif nums[right] > nums[mid]:
                right = mid
            elif nums[left] >= nums[mid]:
                left += 1
            else:
                right -= 1
        return nums[left]
                

        