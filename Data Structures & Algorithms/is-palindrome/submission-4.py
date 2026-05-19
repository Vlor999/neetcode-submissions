class Solution:
    def removeSpace(self, s:str)->str:
        alphaNum = """ ,.<>/?!'\"\\[]{}@£$%^&*(-_)=+#€;:|`~§±"""
        ouput = ""
        for lettre in s:
            if lettre in alphaNum:
                continue
            lowerLettre = lettre.lower()
            ouput += lowerLettre
        return ouput 

    def isPalindrome(self, s: str) -> bool:
        output = True
        sWithoutSpace = self.removeSpace(s)
        taille = len(sWithoutSpace)
        for i in range(taille//2):
            if sWithoutSpace[i] != sWithoutSpace[taille - i - 1]:
                print(sWithoutSpace[i], sWithoutSpace[taille - i - 1])
                return False
        return output