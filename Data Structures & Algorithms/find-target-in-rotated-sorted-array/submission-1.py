class Solution:
    def foundRotation(self, nums: List[int]) -> int:
        """
        Search the index where the rotation appear

        Args:
            List[int]: the rotated array
        
        Return:
            (int) the index to rotate the array
        """
        left = 0
        right = len(nums) - 1
        while nums[left] > nums[right]:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return left

    def search(self, nums: List[int], target: int) -> int:
        i = self.foundRotation(nums)
        nums = nums[i:] + nums[:i]
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return (middle + i) % len(nums)
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1