class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_elems = {}
        t_elems = {}
        for letter in s:
            s_elems[letter] = s_elems.get(letter, 0) + 1
        for letter in t:
            t_elems[letter] = t_elems.get(letter, 0) + 1
        
        for key, value in s_elems.items():
            if key not in t_elems:
                return False 
            if value != t_elems[key]:
                return False
        for key, value in t_elems.items():
            if key not in s_elems:
                return False 
            if value != s_elems[key]:
                return False
        return True