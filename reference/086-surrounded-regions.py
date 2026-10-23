class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
        stack = [(r, c) for r in range(rows) for c in range(cols)
                 if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == "O"]
        safe = set(stack)
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in safe:
                    safe.add((nr, nc))
                    stack.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
