class Solution:
    def eraseOverlapIntervals(self, intervals):
        removed = 0
        last_end = float("-inf")
        for a, b in sorted(intervals, key=lambda iv: iv[1]):
            if a >= last_end:
                last_end = b
            else:
                removed += 1
        return removed
