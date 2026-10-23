class Solution:
    def spiralOrder(self, matrix):
        out = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            out += matrix[top][left:right + 1]
            for r in range(top + 1, bottom + 1):
                out.append(matrix[r][right])
            if top < bottom:
                out += matrix[bottom][left:right][::-1]
            if left < right:
                for r in range(bottom - 1, top, -1):
                    out.append(matrix[r][left])
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return out
