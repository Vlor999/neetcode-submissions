class Solution:
    def isPalindrome(self, s:str)->bool:
        return s == s[::-1]

    def backtracking(self, word:str, debut:int, result:list[list[str]], current:list[str]):
        if debut == len(word):
            result.append(current.copy())
        for i in range(debut, len(word)):
            sub = word[debut: i + 1]
            if self.isPalindrome(sub):
                current.append(sub)
                self.backtracking(word, i + 1, result, current)
                current.pop()


    def partition(self, s: str) -> list[list[str]]:
        result = []
        self.backtracking(s, 0, result, [])
        return result
