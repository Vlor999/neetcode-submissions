class Solution:
    def foundPosition(self, board:list[list[int]], lettre:str) -> list[tuple[int, int]]:
        output = []
        if len(board) == 0:
            return output
        for l in range(len(board)):
            for c in range(len(board[0])):
                if lettre == board[l][c]:
                    output.append((l,c))
        return output
    
    def positionAround(self, board:list[list[int]], position) -> list[tuple[int,int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valid_positions = []
        for d in directions:
            new_row, new_col = position[0] + d[0], position[1] + d[1]
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] != "#":
                valid_positions.append((new_row, new_col))
        return valid_positions

    def foundWordInBoard(self, board:list[list[int]], word, position, lettrePosition):
        if word == "" or lettrePosition >= len(word):
            return True
        postionAround = self.positionAround(board, position)
        for pos in postionAround:
            if board[pos[0]][pos[1]] == word[lettrePosition]:
                board[pos[0]][pos[1]] = "#"
                isGood = self.foundWordInBoard(board, word, pos, lettrePosition + 1)
                if isGood:
                    return True
                board[pos[0]][pos[1]] = word[lettrePosition]
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        listPosition = self.foundPosition(board, word[0])
        for position in listPosition:
            board[position[0]][position[1]] = "#"
            isGood = self.foundWordInBoard(board, word, position, 1)
            if isGood:
                return True
            board[position[0]][position[1]] = word[0]
        return False