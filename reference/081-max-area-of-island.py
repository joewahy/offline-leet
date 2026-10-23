class Solution:
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        seen = set()
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    stack, area = [(r, c)], 0
                    while stack:
                        x, y = stack.pop()
                        area += 1
                        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                stack.append((nx, ny))
                    best = max(best, area)
        return best
