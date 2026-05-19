class Solution:
    def getPosition(self, num:str) -> list[int]:
        listPosition = []
        for i in range(len(num)):
            if num[i] == '1':
                listPosition.append(i)
        return listPosition


    def subsetsWithData(self, listIntBinaire, nums):
        positions = []
        output = [[]]
        for num in listIntBinaire:
            positions.append(self.getPosition(num))
        for pos in positions:
            output.append([nums[i] for i in pos])
        return output

    def subsets(self, nums: list[int]) -> list[list[int]]:
        taille = len(nums)
        nombreValeur = 2 ** taille - 1
        listInt = []
        while nombreValeur > 0:
            valBin = str(bin(nombreValeur))[2:]
            valBin = '0' * (taille - len(valBin)) + valBin 
            listInt.append(valBin)
            nombreValeur -= 1
        return self.subsetsWithData(listInt, nums)