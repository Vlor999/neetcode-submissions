class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, val in enumerate(nums):
            target = -val
            left, right = 0, len(nums) -1
            while left < right:
                val_creat = nums[left] + nums[right]
                if left == right or left == i or right == i:
                    break
                if val_creat == target:
                    out.append(sorted([val, nums[left], nums[right]]))
                if val_creat < target:
                    left += 1
                    if left == i :
                        left += 1
                else:
                    right -= 1
                    if right == i:
                        right -= 1
        out_cleaned = []
        for tri in out:
            if tri not in out_cleaned:
                out_cleaned.append(tri)
        return out_cleaned

        