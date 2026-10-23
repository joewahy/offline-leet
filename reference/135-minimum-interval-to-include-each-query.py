import heapq


class Solution:
    def minInterval(self, intervals, queries):
        intervals = sorted(intervals)
        heap = []
        answers = {}
        i = 0
        for q in sorted(set(queries)):
            while i < len(intervals) and intervals[i][0] <= q:
                a, b = intervals[i]
                heapq.heappush(heap, (b - a + 1, b))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            answers[q] = heap[0][0] if heap else -1
        return [answers[q] for q in queries]
