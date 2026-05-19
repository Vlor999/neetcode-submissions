class Solution:
    def __init__(self):
        pass

    def encode(self, strs: list[str]) -> str:
        outputString = ""
        for elem in strs:
            outputString += elem + "😀"
        return outputString

    def decode(self, s: str) -> list[str]:
        outputList = []
        tailleString = len(s)
        currentString = ""
        for i in range(tailleString):
            elem = s[i]
            if elem == "😀":
                outputList.append(currentString)
                currentString = ""
            else:
                currentString += elem
        return outputList