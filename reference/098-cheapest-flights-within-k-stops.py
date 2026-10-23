import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        best = {}
        heap = [(0, src, 0)]
        while heap:
            cost, u, used = heapq.heappop(heap)
            if u == dst:
                return cost
            if used > k or best.get((u, used), float("inf")) <= cost:
                continue
            best[(u, used)] = cost
            for v, w in graph[u]:
                heapq.heappush(heap, (cost + w, v, used + 1))
        return -1
