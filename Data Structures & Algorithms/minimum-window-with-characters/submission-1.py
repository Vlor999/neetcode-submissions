class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" :
            return ""
        
        countT, window= {}, {}

        for lettre in t:
            countT[lettre] = countT.get(lettre, 0) + 1
        
        have = 0
        need = len(countT)

        result, taille = [-1,-1], float("infinity")

        left = 0
        for right in range(len(s)):
            lettre = s[right]
            window[lettre] = window.get(lettre, 0) + 1 
            if lettre in countT and countT[lettre] == window[lettre]:
                have += 1

            while need == have:
                if (right - left + 1) < taille:
                    result = [left, right]
                    taille = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and countT[s[left]] > window[s[left]]:
                    have -= 1

                left += 1
        l, r = result
        return s[l:r+1] if taille != float("infinity") else ""