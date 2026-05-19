class Solution:
    def backtracking(self, nums: list[int], target: int, current: list[int], result: list[list[int]], start: int):
        if target == 0:
            result.append(current[:])
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            current.append(nums[i])
            self.backtracking(nums, target - nums[i], current, result, i + 1)
            current.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        current = []
        result = []
        self.backtracking(candidates, target, current, result, 0)
        return result