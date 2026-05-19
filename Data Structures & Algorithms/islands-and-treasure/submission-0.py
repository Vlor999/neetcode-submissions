from collections import deque

class Solution:
    def getAround(self, pos: tuple[int, int], grid) -> list[tuple[int, int]]:
        maxX = len(grid)
        maxY = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        around = []
        for dx, dy in directions:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if 0 <= new_x < maxX and 0 <= new_y < maxY and grid[new_x][new_y] != -1:
                around.append((new_x, new_y))
        return around

    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        listPosTreasure = []
        for l in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[l][c] == 0:
                    listPosTreasure.append((l, c))
        if not listPosTreasure:
            return

        for pos in listPosTreasure:
            l, c = pos
            toSee = deque()
            visited = set()
            around = self.getAround(pos, grid)
            toSee.extend(around)
            distance = 1
            while toSee:
                for _ in range(len(toSee)):
                    head = toSee.popleft()
                    if head in visited:
                        continue
                    visited.add(head)
                    grid[head[0]][head[1]] = min(distance, grid[head[0]][head[1]])
                    around = self.getAround(head, grid)
                    toSee.extend(around)
                distance += 1