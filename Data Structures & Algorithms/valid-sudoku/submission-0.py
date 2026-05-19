class Solution:
    def check_line(self, line: list[str]) -> bool:
        counter = {}
        for letter in line:
            if letter == ".":
                continue
            counter[letter] = counter.get(letter, 0) + 1
            if counter[letter] > 1:
                return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check line
        for line in board:
            if not self.check_line(line):
                return False
        # check col
        for i in range(len(board)):
            col = [board[j][i] for j in range(len(board))]
            if not self.check_line(col):
                return False
        # check block
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                block = []
                for ii in range(3):
                    for jj in range(3):
                        block.append(board[i+ii][j+jj])
                if not self.check_line(block):
                    return False
        return True

        