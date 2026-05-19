

class Solution:
    def getAround(self, position, grid):
        l, c = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        around = []
        for dl, dc in directions:
            new_l, new_c = l + dl, c + dc
            if 0 <= new_l < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_l][new_c] == '1':
                around.append((new_l, new_c))
        return around

    def numIslands(self, grid: list[list[str]]) -> int:
        toLook = []
        for l in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[l][c] == '1':
                    toLook.append((l, c))
        if len(toLook) == 0:
            return 0
        compteur = 0
        while toLook:
            current = toLook.pop()
            grid[current[0]][current[1]] = "*"
            getAroundInteresting = self.getAround(current, grid)
            setElem = set(getAroundInteresting)
            while setElem:
                elem = setElem.pop()
                if elem in toLook:
                    toLook.remove(elem)
                grid[elem[0]][elem[1]] = "*"
                newSetElem = set(self.getAround(elem, grid))
                setElem.update(newSetElem)
            compteur += 1
        return compteur