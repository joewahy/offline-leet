from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        rows, cols = len(rooms), len(rooms[0])
        q = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
        while q:
            r, c = q.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
