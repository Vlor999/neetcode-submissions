class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def around_cases(self, heights: list[list[int]], pos: tuple[int, int]) -> list[tuple[int, int]]:
        positions_autour = []
        ligne, colonne = pos
        valeur_actuelle = heights[ligne][colonne]
        for dl, dc in self.directions:
            nouvelle_ligne = ligne + dl
            nouvelle_colonne = colonne + dc
            if 0 <= nouvelle_ligne < len(heights) and 0 <= nouvelle_colonne < len(heights[0]) and heights[nouvelle_ligne][nouvelle_colonne] >= valeur_actuelle:
                positions_autour.append((nouvelle_ligne, nouvelle_colonne))
        return positions_autour
        
    def getTouchedWater(self, heights: list[list[int]], init_position:list[tuple[int]]) -> set[list[int]]:
        touchedWater = set(init_position)
        next_land = set(touchedWater)
        while next_land:
            actuelle = next_land.pop()
            around = self.around_cases(heights, actuelle)
            for pos in around:
                if pos not in touchedWater:
                    next_land.add(pos)
                    touchedWater.add(pos)
        return touchedWater


    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacific_water = [(0, i) for i in range(len(heights[0]))] + [(i, 0) for i in range(len(heights))]

        pacific_touched = self.getTouchedWater(heights, pacific_water)

        atlantic_water = [(len(heights) - 1, i) for i in range(len(heights[0]))] + [(i, len(heights[0]) - 1) for i in range(len(heights))]

        atlantic_touched = self.getTouchedWater(heights, atlantic_water)
        
        intersection_land = pacific_touched.intersection(atlantic_touched)
        output_intersection = [list(position) for position in intersection_land]
        return output_intersection