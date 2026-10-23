class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        best = [float("inf")] * n
        used = [False] * n
        best[0] = 0
        total = 0
        for _ in range(n):
            u = min((i for i in range(n) if not used[i]), key=best.__getitem__)
            used[u] = True
            total += best[u]
            ux, uy = points[u]
            for v in range(n):
                if not used[v]:
                    d = abs(ux - points[v][0]) + abs(uy - points[v][1])
                    if d < best[v]:
                        best[v] = d
        return total
