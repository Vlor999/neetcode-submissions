class Solution:

    def subRec(self, current:list[int], position:int, nums: list[int], result:list[list[int]]):
        result.append(current[:])
        for i in range(position, len(nums)):
            current.append(nums[i])
            self.subRec(current, i + 1, nums, result)
            current.pop()


    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []
        position = 0
        self.subRec(current, position, nums, result)
        return result