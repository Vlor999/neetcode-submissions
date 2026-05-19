class Solution:
    def convListToString(self, position: list[int]) -> str:
        return f"{position[0]}/{position[1]}"

    def convStringToList(self, stringPosition: str) -> list[int]:
        return list(map(int, stringPosition.split("/")))
    
    def positionAutour(self, nombreLigne: int, nombreColonne: int, position: list[int], alreadySeen: set[str]) -> list[list[int]]:
        l, c = position
        output = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dl, dc in directions:
            new_l, new_c = l + dl, c + dc
            new_pos_str = self.convListToString([new_l, new_c])
            if 0 <= new_l < nombreLigne and 0 <= new_c < nombreColonne and new_pos_str not in alreadySeen:
                output.append([new_l, new_c])
        
        return output

    def findWord(self, board: list[list[str]], word: str) -> bool:
        nombreLigne, nombreColonne = len(board), len(board[0])
        start_positions = [[l, c] for l in range(nombreLigne) for c in range(nombreColonne) if board[l][c] == word[0]]
        
        if not start_positions:
            return False
        
        for start_pos in start_positions:
            toSee = [(0, {self.convListToString(start_pos)}, start_pos)]
            
            while toSee:
                posLettre, alreadySeenCurrent, possiblePosition = toSee.pop()
                
                if posLettre == len(word) - 1:
                    return True
                
                next_char = word[posLettre + 1]
                for next_pos in self.positionAutour(nombreLigne, nombreColonne, possiblePosition, alreadySeenCurrent):
                    if board[next_pos[0]][next_pos[1]] == next_char:
                        new_seen = alreadySeenCurrent.copy()
                        new_seen.add(self.convListToString(next_pos))
                        toSee.append((posLettre + 1, new_seen, next_pos))
        
        return False

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        if len(board) == 0:
            return []
        return [word for word in words if self.findWord(board, word)]
