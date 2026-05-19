class Solution:
    letters:str = "abcdefghijklmnopqrstuvwxyz0123456789"
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join(s.split()).lower()
        cleaned_sentence = ""
        for letter in sentence:
            if letter not in self.letters:
                continue
            cleaned_sentence += letter
        return cleaned_sentence == cleaned_sentence[::-1]