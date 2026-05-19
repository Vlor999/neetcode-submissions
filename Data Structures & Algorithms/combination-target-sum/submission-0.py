class Solution:
    def updateList(self, nums: list[int], target: int) -> list[int]:
        newList = []
        for elem in nums:
            if elem <= target:
                newList.append(elem)
        return newList

    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        if target == 0:
            return [[]]
        nums = self.updateList(nums, target)
        output = set()
        if target in nums:
            output.add(tuple(sorted([target])))
        for nombre in nums:
            listToHere = self.combinationSum(nums, target - nombre)
            for combination in listToHere:
                output.add(tuple(sorted(combination + [nombre])))
        return [list(comb) for comb in output]