class Solution:
    def classiqueSearch(self, nums: list[int], target: int, debut: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid + debut
        return -1

    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        if target >= nums[pivot] and target <= nums[-1]:
            return self.classiqueSearch(nums[pivot:], target, pivot)
        else:
            return self.classiqueSearch(nums[:pivot], target, 0)
        