class Solution:
    def blockPos(self, board: list[str], pos: tuple[int, int]) -> list[str]:
        l, c = pos[0], pos[1]
        newBoard = [row[:] for row in board]
        for i in range(len(board)):
            newBoard[l] = newBoard[l][:i] + "X" + newBoard[l][i + 1:]
            newBoard[i] = newBoard[i][:c] + "X" + newBoard[i][c + 1:]
            if l + i < len(board) and c + i < len(board):
                newBoard[l + i] = newBoard[l + i][:c + i] + "X" + newBoard[l + i][c + i + 1:]
            if l - i >= 0 and c + i < len(board):
                newBoard[l - i] = newBoard[l - i][:c + i] + "X" + newBoard[l - i][c + i + 1:]
            if l + i < len(board) and c - i >= 0:
                newBoard[l + i] = newBoard[l + i][:c - i] + "X" + newBoard[l + i][c - i + 1:]
            if l - i >= 0 and c - i >= 0:
                newBoard[l - i] = newBoard[l - i][:c - i] + "X" + newBoard[l - i][c - i + 1:]
        newBoard[l] = newBoard[l][:c] + "Q" + newBoard[l][c + 1:]
        return newBoard

    def backtracking(self, board: list[str], result: list[list[str]], row: int):
        if row == len(board):
            result.append(["".join(row.replace("X", ".")) for row in board])
            return
        for col in range(len(board)):
            if board[row][col] == ".":
                temp = [row[:] for row in board]
                board = self.blockPos(board, (row, col))
                self.backtracking(board, result, row + 1)
                board = temp

    def solveNQueens(self, n: int) -> list[list[str]]:
        board = ["." * n for _ in range(n)]
        result = []
        self.backtracking(board, result, 0)
        return result