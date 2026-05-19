class Solution:
    def backtracking(self, nums: list[int], current:list[int], result:list[list[int]], tailleInit:int):
        if len(current) == tailleInit:
            result.append(current[:])
            return
        for num in nums:
            current.append(num)
            copyNums = nums[:]
            copyNums.remove(num)
            self.backtracking(copyNums, current, result, tailleInit)
            current.pop()

    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []
        self.backtracking(nums, current, result, len(nums))
        return result