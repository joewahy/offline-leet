class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = {r for r in range(rows) for c in range(cols) if matrix[r][c] == 0}
        zero_cols = {c for r in range(rows) for c in range(cols) if matrix[r][c] == 0}
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
