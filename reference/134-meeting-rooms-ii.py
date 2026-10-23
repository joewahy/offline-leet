class Solution:
    def minMeetingRooms(self, intervals):
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        rooms = best = j = 0
        for s in starts:
            while ends[j] <= s:
                j += 1
                rooms -= 1
            rooms += 1
            best = max(best, rooms)
        return best
