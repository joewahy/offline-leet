class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def go(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            best = 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + go(nr, nc))
            memo[(r, c)] = best
            return best

        return max(go(r, c) for r in range(rows) for c in range(cols))
