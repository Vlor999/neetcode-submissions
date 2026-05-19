class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        left_val = 1
        right_val = 1
        for i in range(len(nums)):
            left_val *= nums[i]
            right_val *= nums[len(nums) - i - 1]
            left.append(left_val)
            right.append(right_val)
        right.reverse()
        out = []
        for i in range(len(nums)):
            val = left[i] * right[i + 1]
            out.append(val)
        return out
            