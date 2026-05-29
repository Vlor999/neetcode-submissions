class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = []
        for l in matrix:
            line += l
        left, right = 0, len(line) - 1
        while left < right:
            mid = (left + right) // 2
            if line[mid] == target:
                return True
            elif line[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return line[left] == target