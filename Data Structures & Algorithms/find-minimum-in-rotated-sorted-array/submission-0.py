class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[right]: 
                return nums[left]
            if nums[mid] > nums[left]:
                left = mid
            else :
                right = mid
            print(left,right)
        return nums[(left + 1) % len(nums)]
        