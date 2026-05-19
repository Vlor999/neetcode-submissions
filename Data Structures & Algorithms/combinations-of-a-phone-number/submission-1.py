class Solution:
    def __init__(self):
        self.equivalence = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz", 
        }
    
    def backtracking(self, digits: str, result:list[str], current:str, position:int):
        if position >= len(digits):
            result.append(current[:])
            return
        for lettre in self.equivalence[digits[position]]:
            current += lettre
            self.backtracking(digits, result, current, position + 1)
            current = current[:-1]

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        result = []
        current = ""
        self.backtracking(digits, result, current, 0)
        return result