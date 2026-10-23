class Solution:
    def solveNQueens(self, n):
        out = []
        cols, diag, anti = set(), set(), set()
        placed = []

        def go(r):
            if r == n:
                out.append(["." * c + "Q" + "." * (n - c - 1) for c in placed])
                return
            for c in range(n):
                if c in cols or r - c in diag or r + c in anti:
                    continue
                cols.add(c), diag.add(r - c), anti.add(r + c)
                placed.append(c)
                go(r + 1)
                placed.pop()
                cols.remove(c), diag.remove(r - c), anti.remove(r + c)

        go(0)
        return out
