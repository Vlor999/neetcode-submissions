class Solution:
    def updateList(self, listElem, area) -> list:
        return [elem for elem in listElem if elem[2] > area]

    def foundBest(self, listPossible, currentElem) -> int:
        print(listPossible)
        i, h, _ = currentElem
        area = 0
        for iCurrent, hCurrent, _ in listPossible:
            currentArea = abs(iCurrent - i) * min(h, hCurrent)
            if currentArea > area:
                area = currentArea
            print(currentArea)
                
        return area

    def maxArea(self, heights: list[int]) -> int:
        areaMax = 0
        listeCouple = []
        taille = len(heights)
        
        for i, h in enumerate(heights):
            maxPossible = h * max(taille - i, i)
            listeCouple.append((i, h, maxPossible))
        
        listeCouple.sort(key=lambda x: x[2], reverse=True)
        elem0, elem1 = listeCouple[:2]
        areaMax = abs(elem0[0] - elem1[0]) * min(elem0[1], elem1[1])
        
        listePossible = self.updateList(listeCouple, areaMax)
        
        while listePossible:
            elem0 = listePossible[0]
            currentArea = self.foundBest(listePossible, elem0)
            if currentArea > areaMax:
                areaMax = currentArea
            listePossible = listePossible[1:]
            listePossible = self.updateList(listePossible, areaMax)
        return areaMax