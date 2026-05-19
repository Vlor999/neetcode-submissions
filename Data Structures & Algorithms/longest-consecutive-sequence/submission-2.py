class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        values = set(nums)
        mini = min(nums) - 2
        max_length = 0
        for val in values:
            current_length = 1
            mini = val
            while mini + 1 in values:
                current_length += 1
                mini += 1
            max_length = max(max_length, current_length)
        return max_length