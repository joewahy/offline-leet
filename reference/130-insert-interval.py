class Solution:
    def insert(self, intervals, newInterval):
        out = []
        start, end = newInterval
        i = 0
        while i < len(intervals) and intervals[i][1] < start:
            out.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        out.append([start, end])
        out += intervals[i:]
        return out
