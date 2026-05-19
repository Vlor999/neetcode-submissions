class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        position = -1

        while up <= down:
            mid = (up+down)//2
            if matrix[mid][0] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                position = mid
                break
        
        if position != -1:
            return True
        
        
        listGauche = matrix[max(down, 0)]
        listDroite = matrix[min(up, len(matrix) - 1)]

        if listGauche[0] != listDroite[0]:
            listeElem = listGauche + listDroite
        else:
            listeElem = listGauche
        left, right = 0, len(listeElem) - 1

        while left <= right:
            mid = (left+right)//2
            if listeElem[mid] < target:
                left = left + 1
            elif listeElem[mid] > target:
                right = right - 1
            else:
                return True
        return False
