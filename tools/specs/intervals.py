from spec import P

CATEGORY = "intervals"


def _disjoint(rng, m, span):
    pts = sorted(rng.sample(range(span), 2 * m))
    return [[pts[2 * i], pts[2 * i + 1]] for i in range(m)]


def _insert_case(rng, m, span):
    iv = _disjoint(rng, m, span) if m else []
    a = rng.randint(0, span)
    return [iv, [a, a + rng.randint(0, span // 4)]]


def _rand_intervals(rng, n, span, maxlen):
    out = []
    for _ in range(n):
        a = rng.randint(0, span)
        out.append([a, a + rng.randint(0, maxlen)])
    return out


def _erase_pairs(rng, n, span, maxlen):
    out = []
    for _ in range(n):
        a = rng.randint(0, span)
        out.append([a, a + rng.randint(1, maxlen)])
    return out


def _rooms_disjoint(rng, n, span):
    pts = sorted(rng.sample(range(span), 2 * n))
    iv = [[pts[2 * i], pts[2 * i + 1]] for i in range(n)]
    rng.shuffle(iv)
    return iv


def _min_interval(rng, n, q, span):
    iv = []
    for _ in range(n):
        a = rng.randint(1, span)
        iv.append([a, a + rng.randint(0, span // 5)])
    return [iv, [rng.randint(1, span + span // 5) for _ in range(q)]]


PROBLEMS = [
    P(130, "Insert Interval", "Medium", "insert",
      r'''
`intervals` is a list of non-overlapping intervals `[start, end]`, sorted by `start`. Insert `newInterval` into it so the list stays sorted and has no overlaps, merging any intervals that overlap (intervals that only touch at an endpoint, like `[1, 2]` and `[2, 3]`, also merge).

Return the resulting list of intervals.

## Examples

```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Constraints

- `0 <= len(intervals) <= 10000`
- `0 <= start <= end <= 10^5`
- `intervals` is sorted by `start` and has no overlaps.

## Hints

- Copy the intervals that end before the new one starts, merge everything that overlaps it, then copy the rest.
''',
      r'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pass
''',
      r'''
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
''',
      [([[[1, 3], [6, 9]], [2, 5]], [[1, 5], [6, 9]]),
       ([[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]], [[1, 2], [3, 10], [12, 16]]), ([[], [5, 7]], [[5, 7]]),
       ([[[1, 5]], [2, 3]], [[1, 5]]), ([[[1, 5]], [6, 8]], [[1, 5], [6, 8]]), ([[[3, 5]], [1, 2]], [[1, 2], [3, 5]]),
       ([[[1, 5]], [5, 7]], [[1, 7]]), ([[[1, 2], [3, 4]], [2, 3]], [[1, 4]])],
      gen=lambda rng: [_insert_case(rng, m, 60) for m in (0, 1, 3, 6, 10)] + [_insert_case(rng, 5000, 100000), _insert_case(rng, 5000, 100000)],
      small=lambda rng: _insert_case(rng, rng.randint(0, 5), 40),
      brute=r'''
class Solution:
    def insert(self, intervals, newInterval):
        items = sorted(intervals + [newInterval])
        out = [items[0]]
        for a, b in items[1:]:
            if a <= out[-1][1]:
                out[-1] = [out[-1][0], max(out[-1][1], b)]
            else:
                out.append([a, b])
        return out
'''),

    P(131, "Merge Intervals", "Medium", "merge",
      r'''
Given a list of intervals `[start, end]` in any order, merge all intervals that overlap (intervals that only touch at an endpoint, like `[1, 2]` and `[2, 3]`, also merge) and return the merged intervals sorted by `start`.

## Examples

```
Input:  intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]

Input:  intervals = [[1,2],[2,3]]
Output: [[1,3]]
```

## Constraints

- `1 <= len(intervals) <= 10000`
- `0 <= start <= end <= 10^6`

## Hints

- Sort by start. Then each interval either extends the last merged one or begins a new one.
''',
      r'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def merge(self, intervals):
        out = []
        for a, b in sorted(intervals):
            if out and a <= out[-1][1]:
                out[-1][1] = max(out[-1][1], b)
            else:
                out.append([a, b])
        return out
''',
      [([[[1, 3], [1, 5], [6, 7]]], [[1, 5], [6, 7]]), ([[[1, 2], [2, 3]]], [[1, 3]]), ([[[1, 4], [4, 5]]], [[1, 5]]),
       ([[[1, 4], [0, 4]]], [[0, 4]]), ([[[1, 4], [2, 3]]], [[1, 4]]), ([[[1, 2]]], [[1, 2]]),
       ([[[8, 10], [1, 3], [2, 6], [15, 18]]], [[1, 6], [8, 10], [15, 18]]), ([[[1, 4], [0, 0]]], [[0, 0], [1, 4]])],
      gen=lambda rng: [[_rand_intervals(rng, n, 30, 5)] for n in (3, 6, 10, 20)]
      + [[_rand_intervals(rng, 10000, 1000000, 150)], [_rand_intervals(rng, 10000, 1000000, 5000)]],
      small=lambda rng: [_rand_intervals(rng, rng.randint(1, 7), 20, 4)],
      brute=r'''
class Solution:
    def merge(self, intervals):
        items = [list(i) for i in intervals]
        changed = True
        while changed:
            changed = False
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    a, b = items[i], items[j]
                    if a[0] <= b[1] and b[0] <= a[1]:
                        items[i] = [min(a[0], b[0]), max(a[1], b[1])]
                        items.pop(j)
                        changed = True
                        break
                if changed:
                    break
        return sorted(items)
'''),

    P(132, "Non-overlapping Intervals", "Medium", "eraseOverlapIntervals",
      r'''
Given a list of intervals `[start, end]`, return the minimum number of intervals you must remove so that the remaining ones do not overlap. Intervals that only touch at an endpoint (like `[1, 2]` and `[2, 3]`) do not overlap.

## Examples

```
Input:  intervals = [[1,2],[2,4],[1,4]]
Output: 1          # remove [1,4]

Input:  intervals = [[1,2],[1,2],[1,2]]
Output: 2
```

## Constraints

- `1 <= len(intervals) <= 10000`
- `0 <= start < end <= 10^6`

## Hints

- Greedy: sort by end. Keep an interval if it starts at or after the end of the last kept one; otherwise remove it.
''',
      r'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass
''',
      r'''
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
''',
      [([[[1, 2], [2, 4], [1, 4]]], 1), ([[[1, 2], [2, 4]]], 0), ([[[1, 2], [1, 2], [1, 2]]], 2),
       ([[[1, 2], [2, 3], [3, 4], [1, 3]]], 1), ([[[1, 100], [11, 22], [1, 11], [2, 12]]], 2), ([[[1, 2]]], 0),
       ([[[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]], 2)],
      gen=lambda rng: [[_erase_pairs(rng, n, 25, 6)] for n in (3, 6, 10, 15)]
      + [[_erase_pairs(rng, 10000, 1000000, 300)], [_erase_pairs(rng, 10000, 1000, 20)]],
      small=lambda rng: [_erase_pairs(rng, rng.randint(1, 9), 15, 5)],
      brute=r'''
class Solution:
    def eraseOverlapIntervals(self, intervals):
        n = len(intervals)
        best = 0
        for mask in range(1 << n):
            chosen = sorted(intervals[i] for i in range(n) if mask >> i & 1)
            if all(chosen[k][1] <= chosen[k + 1][0] for k in range(len(chosen) - 1)):
                best = max(best, len(chosen))
        return n - best
'''),

    P(133, "Meeting Rooms", "Easy", "canAttendMeetings",
      r'''
You are given a list of meeting time intervals, each an `Interval` object with `start` and `end` attributes (the meeting occupies `[start, end)`). Return `True` if one person can attend all the meetings, i.e. no two meetings overlap. A meeting that starts exactly when another ends does not overlap it.

In the tests an interval is written as `[start, end]`.

## Examples

```
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: False

Input:  intervals = [[5,8],[9,15]]
Output: True
```

## Constraints

- `0 <= len(intervals) <= 8000`
- `0 <= start < end <= 10^6`

## Hints

- Sort by start time, then compare each meeting with the one before it.
''',
      r'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        pass
''',
      r'''
class Solution:
    def canAttendMeetings(self, intervals):
        ordered = sorted(intervals, key=lambda i: i.start)
        return all(a.end <= b.start for a, b in zip(ordered, ordered[1:]))
''',
      [([[[0, 30], [5, 10], [15, 20]]], False), ([[[5, 8], [9, 15]]], True), ([[]], True), ([[[1, 2]]], True),
       ([[[1, 5], [5, 10]]], True), ([[[1, 5], [4, 10]]], False), ([[[7, 10], [2, 4]]], True), ([[[1, 10], [2, 3]]], False)],
      arg_types=["intervals"],
      gen=lambda rng: [[_rooms_disjoint(rng, n, 100)] for n in (2, 5, 10)] + [[_erase_pairs(rng, n, 30, 6)] for n in (3, 6)]
      + [[_rooms_disjoint(rng, 8000, 1000000)], [_rooms_disjoint(rng, 8000, 1000000)[:-1] + [[0, 1000000]]]],
      small=lambda rng: [_erase_pairs(rng, rng.randint(0, 6), 15, 5)],
      brute=r'''
class Solution:
    def canAttendMeetings(self, intervals):
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                a, b = intervals[i], intervals[j]
                if a.start < b.end and b.start < a.end:
                    return False
        return True
'''),

    P(134, "Meeting Rooms II", "Medium", "minMeetingRooms",
      r'''
You are given a list of meeting time intervals, each an `Interval` object with `start` and `end` attributes (the meeting occupies `[start, end)`). Return the minimum number of rooms needed so that all meetings can take place. A meeting that starts exactly when another ends can reuse its room.

In the tests an interval is written as `[start, end]`.

## Examples

```
Input:  intervals = [[0,40],[5,10],[15,20]]
Output: 2

Input:  intervals = [[4,9]]
Output: 1
```

## Constraints

- `0 <= len(intervals) <= 8000`
- `0 <= start < end <= 10^6`

## Hints

- Sort the start times and the end times separately, then sweep through them, counting how many meetings are running at once.
''',
      r'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        pass
''',
      r'''
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
''',
      [([[[0, 40], [5, 10], [15, 20]]], 2), ([[[4, 9]]], 1), ([[]], 0), ([[[1, 5], [5, 10]]], 1),
       ([[[1, 5], [2, 6], [3, 7]]], 3), ([[[0, 30], [5, 10], [15, 20]]], 2), ([[[7, 10], [2, 4]]], 1),
       ([[[1, 2], [1, 2], [1, 2]]], 3), ([[[1, 10], [2, 3], [4, 5], [6, 7]]], 2)],
      arg_types=["intervals"],
      gen=lambda rng: [[_erase_pairs(rng, n, 30, 8)] for n in (3, 6, 10, 15)]
      + [[_erase_pairs(rng, 8000, 1000000, 20000)], [_erase_pairs(rng, 8000, 1000, 100)]],
      small=lambda rng: [_erase_pairs(rng, rng.randint(0, 7), 15, 5)],
      brute=r'''
class Solution:
    def minMeetingRooms(self, intervals):
        best = 0
        for t in {i.start for i in intervals}:
            best = max(best, sum(1 for i in intervals if i.start <= t < i.end))
        return best
'''),

    P(135, "Minimum Interval to Include Each Query", "Hard", "minInterval",
      r'''
`intervals[i] = [left, right]` is a closed interval whose size is `right - left + 1`. For each value in `queries`, find the size of the smallest interval that contains it (`left <= query <= right`). If no interval contains the query, the answer for it is `-1`.

Return the answers in the same order as `queries`.

## Examples

```
Input:  intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,4,6]
Output: [2, 2, 3, 5, 1]

Input:  intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2, -1, 4, 6]
```

## Constraints

- `1 <= len(intervals), len(queries) <= 7000`
- `1 <= left <= right <= 10^6`
- `1 <= queries[j] <= 10^6`

## Hints

- Answer the queries in increasing order. Sweep over the intervals sorted by `left`, pushing each into a min-heap keyed by size, and discard heap tops that end before the query.
''',
      r'''
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        pass
''',
      r'''
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
''',
      [([[[1, 3], [2, 3], [3, 7], [6, 6]], [2, 3, 1, 4, 6]], [2, 2, 3, 5, 1]),
       ([[[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]], [2, -1, 4, 6]), ([[[1, 1]], [1]], [1]),
       ([[[1, 1]], [2]], [-1]), ([[[1, 10], [2, 4]], [3, 10, 0]], [3, 10, -1]), ([[[5, 5], [1, 10]], [5, 1]], [1, 10])],
      gen=lambda rng: [_min_interval(rng, n, q, 30) for n, q in ((3, 5), (6, 8), (10, 12))]
      + [_min_interval(rng, 7000, 7000, 1000000), _min_interval(rng, 7000, 7000, 50000)],
      small=lambda rng: _min_interval(rng, rng.randint(1, 6), rng.randint(1, 6), 12),
      brute=r'''
class Solution:
    def minInterval(self, intervals, queries):
        out = []
        for q in queries:
            sizes = [b - a + 1 for a, b in intervals if a <= q <= b]
            out.append(min(sizes) if sizes else -1)
        return out
'''),
]
