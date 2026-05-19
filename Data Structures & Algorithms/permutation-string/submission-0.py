#! /usr/bin/env python3

class Solution:

    def isValid(self, dicoElem):
        for key in dicoElem:
            if dicoElem[key] != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        taille1 = len(s1)
        taille2 = len(s2)

        if taille1 > taille2:
            return False
        
        #On a forcément un string 1 plus petit que le 2

        dicoElem = {}
        for lettre in s1:
            if lettre not in dicoElem:
                dicoElem[lettre] = 1
            else :
                dicoElem[lettre] += 1

        left = 0
        right = taille1
        window = s2[left:right]

        succes = False

        for lettre in window:
            if lettre in dicoElem:
                dicoElem[lettre] -= 1
        
        succes = self.isValid(dicoElem)
        while right <= taille2 and not succes:
            oldLettre = s2[left]
            if right + 1 > taille2:
                break
            newLettre = s2[right]

            if oldLettre in dicoElem:
                dicoElem[oldLettre] += 1
            if newLettre in dicoElem:
                dicoElem[newLettre] -= 1

            succes = self.isValid(dicoElem)
            left += 1
            right += 1
        return succes

