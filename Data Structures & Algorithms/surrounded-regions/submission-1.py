class Solution:
    def getArround(self, board: list[list[str]], current: tuple[int, int]) -> list[tuple[int, int]]:
        l, c = current
        output = []
        candidates = [(l - 1, c), (l + 1, c), (l, c - 1), (l, c + 1)]
        for li, ci in candidates:
            if 0 <= li < len(board) and 0 <= ci < len(board[0]):
                output.append((li, ci))
        return output

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        for l in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[l][c] == "O":
                    zeros: set[tuple[int, int]] = set()
                    zeros.add((l, c))
                    toLook: set[tuple[int, int]] = set()
                    toLook.add((l, c))
                    alreadySeen: set[tuple[int, int]] = set()
                    isSurrounded = True

                    while toLook:
                        curr = toLook.pop()
                        if curr in alreadySeen:
                            continue
                        alreadySeen.add(curr)
                        around = self.getArround(board, curr)
                        isSurrounded &= len(around) == 4
                        for elem in around:
                            li, ci = elem
                            if board[li][ci] == "O":
                                zeros.add(elem)

                                toLook.add(elem)

                    if isSurrounded:
                        for pos in zeros:
                            li, ci = pos
                            board[li][ci] = "X"