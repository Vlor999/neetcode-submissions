class Solution:
    def backtracking(self, nums: list[int], result: set[tuple[int]], current: list[int], pos: int):
        result.add(tuple(current))  # Use tuple instead of converting to string
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            current.append(nums[i])
            self.backtracking(nums, result, current, i + 1)
            current.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort to handle duplicates
        result = set()
        self.backtracking(nums, result, [], 0)
        return [list(subset) for subset in result]
