class Solution:
    def convListToString(self, listElem:list[int]) -> str:
        output = ""
        for chiffre in listElem:
            output += str(chiffre) + ";"
        return output[:-1]
    
    def convStringToList(self, stringElem:str) ->list[int]:
        if stringElem == "":
            return []
        decompressed = stringElem.split(";")
        listElem = [int(elem) for elem in decompressed]
        return listElem

    def backtracking(self, nums:list[int], result:set[list[int]], current:list[int], pos:int):
        result.add(self.convListToString(sorted(current)))
        for i in range(pos, len(nums)):
            current.append(nums[i])
            self.backtracking(nums, result, current, i + 1)
            current.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = set()
        current = []
        pos = 0
        self.backtracking(nums, result, current, pos)
        return [self.convStringToList(elem) for elem in result]