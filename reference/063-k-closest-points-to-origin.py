import heapq


class Solution:
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])
