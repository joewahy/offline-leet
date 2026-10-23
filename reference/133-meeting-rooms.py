class Solution:
    def canAttendMeetings(self, intervals):
        ordered = sorted(intervals, key=lambda i: i.start)
        return all(a.end <= b.start for a, b in zip(ordered, ordered[1:]))
