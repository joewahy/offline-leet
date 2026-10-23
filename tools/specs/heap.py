from spec import P

CATEGORY = "heap-priority-queue"


def _kth(rng, k, m, lo=-20, hi=20):
    n0 = rng.randint(max(k - 1, 0), k + 3)
    nums = [rng.randint(lo, hi) for _ in range(n0)]
    return [["KthLargest"] + ["add"] * m, [[k, nums]] + [[rng.randint(lo, hi)] for _ in range(m)]]


def _stones(rng, n, hi):
    return [[rng.randint(1, hi) for _ in range(n)]]


def _points(rng, n, k, span):
    while True:
        pts = [[rng.randint(-span, span), rng.randint(-span, span)] for _ in range(n)]
        d = sorted(x * x + y * y for x, y in pts)
        if k == n or d[k - 1] != d[k]:
            return [pts, k]


def _sched(rng, n_tasks, letters, n):
    return [[rng.choice(letters) for _ in range(n_tasks)], n]


def _twitter(rng, m, users=4):
    ops, params, tid = ["Twitter"], [[]], 0
    for _ in range(m):
        r = rng.random()
        u = rng.randint(1, users)
        if r < 0.45:
            tid += 1
            ops.append("postTweet")
            params.append([u, tid])
        elif r < 0.7:
            ops.append("getNewsFeed")
            params.append([u])
        else:
            v = rng.choice([x for x in range(1, users + 1) if x != u])
            ops.append(rng.choice(["follow", "follow", "unfollow"]))
            params.append([u, v])
    return [ops, params]


def _median(rng, m):
    ops, params = ["MedianFinder"], [[]]
    for i in range(m):
        if i % 3 == 2 or rng.random() < 0.3:
            ops.append("findMedian")
            params.append([])
        else:
            ops.append("addNum")
            params.append([rng.randint(-50, 50)])
    ops.append("findMedian")
    params.append([])
    if "addNum" not in ops:
        ops.insert(1, "addNum")
        params.insert(1, [1])
    # a median query needs at least one number first
    seen = False
    for i, op in enumerate(ops):
        if op == "addNum":
            seen = True
        elif op == "findMedian" and not seen:
            ops[i], params[i] = "addNum", [rng.randint(-50, 50)]
            seen = True
    return [ops, params]


PROBLEMS = [
    P(61, "Kth Largest Element in a Stream", "Easy", "KthLargest",
      r'''
Design a class that tracks the `k`-th largest value in a stream of integers. It is the `k`-th largest in sorted order, not the `k`-th distinct value.

Implement `KthLargest`:

- `KthLargest(k, nums)` starts with the integer `k` and the initial stream `nums`.
- `add(val)` appends `val` to the stream and returns the `k`-th largest value seen so far.

## Examples

```
KthLargest(3, [1, 2, 3, 3])
add(3)   -> 3
add(5)   -> 3
add(6)   -> 3
add(7)   -> 5
add(8)   -> 6
```

## Constraints

- `1 <= k <= 1000`
- `0 <= len(nums) <= 1000`, and the stream always has at least `k` values when `add` is called
- `-1000 <= val <= 1000`
- At most `1000` calls to `add`.

## Hints

- A min-heap of size `k` keeps the `k` largest values; its smallest element is the answer.
''',
      r'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass
''',
      r'''
import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
''',
      [([["KthLargest", "add", "add", "add", "add", "add"], [[3, [1, 2, 3, 3]], [3], [5], [6], [7], [8]]],
        [None, 3, 3, 3, 5, 6]),
       ([["KthLargest", "add", "add", "add", "add", "add"], [[1, []], [-3], [-2], [-4], [0], [4]]],
        [None, -3, -2, -2, 0, 4]),
       ([["KthLargest", "add", "add", "add", "add", "add"], [[2, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]],
        [None, 5, 5, 8, 9, 9])],
      design="KthLargest",
      gen=lambda rng: [_kth(rng, k, m) for k, m in ((1, 20), (2, 40), (5, 100), (50, 1000))],
      small=lambda rng: _kth(rng, rng.randint(1, 4), rng.randint(1, 10)),
      brute=r'''
class KthLargest:
    def __init__(self, k, nums):
        self.k, self.nums = k, list(nums)

    def add(self, val):
        self.nums.append(val)
        return sorted(self.nums, reverse=True)[self.k - 1]
'''),

    P(62, "Last Stone Weight", "Easy", "lastStoneWeight",
      r'''
You have a pile of stones with the given positive weights. Repeat this until at most one stone is left: take the two heaviest stones `x <= y` and smash them together.

- If `x == y`, both stones are destroyed.
- Otherwise the stone of weight `x` is destroyed and the other becomes weight `y - x`.

Return the weight of the last remaining stone, or `0` if none remain.

## Examples

```
Input:  stones = [2, 3, 6, 2, 4]
Output: 1

Input:  stones = [1, 2]
Output: 1
```

## Constraints

- `1 <= len(stones) <= 1000`
- `1 <= stones[i] <= 1000`

## Hints

- You repeatedly need the largest elements. A max-heap (use negated values with `heapq`) is the natural fit.
''',
      r'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pass
''',
      r'''
import heapq


class Solution:
    def lastStoneWeight(self, stones):
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            if y != x:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0
''',
      [([[2, 3, 6, 2, 4]], 1), ([[1, 2]], 1), ([[1]], 1), ([[2, 2]], 0), ([[10, 4, 2, 10]], 2),
       ([[7, 6, 7, 6, 9]], 3), ([[1, 1, 1]], 1), ([[5, 5, 5]], 5), ([[3, 7, 2]], 2)],
      gen=lambda rng: [_stones(rng, n, 20) for n in (3, 6, 10, 30)] + [_stones(rng, 1000, 1000)],
      small=lambda rng: _stones(rng, rng.randint(1, 8), 12),
      brute=r'''
class Solution:
    def lastStoneWeight(self, stones):
        s = sorted(stones)
        while len(s) > 1:
            y, x = s.pop(), s.pop()
            if y != x:
                s.append(y - x)
                s.sort()
        return s[0] if s else 0
'''),

    P(63, "K Closest Points to Origin", "Medium", "kClosest",
      r'''
`points[i] = [x, y]` is a point on a 2D plane. Return the `k` points closest to the origin `(0, 0)` by straight-line (Euclidean) distance. The answer may be in any order.

The answer is guaranteed to be unique: there is no tie for the `k`-th closest point.

## Examples

```
Input:  points = [[0, 2], [2, 0], [2, 2]], k = 2
Output: [[0, 2], [2, 0]]

Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
```

## Constraints

- `1 <= k <= len(points) <= 10000`
- `-10000 <= x, y <= 10000`

## Hints

- You can compare squared distances; no square root is needed.
- A max-heap of size `k` (or `heapq.nsmallest`) avoids sorting everything.
''',
      r'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass
''',
      r'''
import heapq


class Solution:
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])
''',
      [([[[0, 2], [2, 0], [2, 2]], 2], [[0, 2], [2, 0]]), ([[[1, 3], [-2, 2]], 1], [[-2, 2]]),
       ([[[3, 3], [5, -1], [-2, 4]], 2], [[3, 3], [-2, 4]]), ([[[1, 1]], 1], [[1, 1]]),
       ([[[0, 1], [1, 0], [5, 5]], 3], [[0, 1], [1, 0], [5, 5]]), ([[[1, 0], [0, 3], [-4, 0], [0, -5]], 2], [[1, 0], [0, 3]])],
      compare="unordered",
      gen=lambda rng: [_points(rng, n, rng.randint(1, n - 1), 20) for n in (4, 8, 15)]
      + [_points(rng, 10000, 100, 10000), _points(rng, 5000, 3, 10000)],
      small=lambda rng: _points(rng, (n := rng.randint(2, 8)), rng.randint(1, n - 1), 9),
      brute=r'''
class Solution:
    def kClosest(self, points, k):
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
'''),

    P(64, "Kth Largest Element in an Array", "Medium", "findKthLargest",
      r'''
Given an integer list `nums` and an integer `k`, return the `k`-th largest element in sorted order (not the `k`-th distinct element).

## Examples

```
Input:  nums = [2, 3, 1, 5, 4], k = 2
Output: 4

Input:  nums = [2, 3, 1, 1, 5, 5, 4], k = 3
Output: 4
```

## Constraints

- `1 <= k <= len(nums) <= 10000`
- `-10000 <= nums[i] <= 10000`

## Hints

- Sorting is O(n log n). A min-heap of size `k` or quickselect can do better.
''',
      r'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass
''',
      r'''
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap[0]
''',
      [([[2, 3, 1, 5, 4], 2], 4), ([[2, 3, 1, 1, 5, 5, 4], 3], 4), ([[1], 1], 1),
       ([[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], 4), ([[5, 5, 5], 2], 5), ([[-1, -2, -3], 3], -3),
       ([[7, 6, 5, 4, 3, 2, 1], 7], 1)],
      gen=lambda rng: [[[rng.randint(-9, 9) for _ in range(n)], rng.randint(1, n)] for n in (3, 8, 15)]
      + [[[rng.randint(-10000, 10000) for _ in range(10000)], 1], [[rng.randint(-10000, 10000) for _ in range(10000)], 5000],
         [[rng.randint(-10000, 10000) for _ in range(10000)], 10000]],
      small=lambda rng: (lambda n: [[rng.randint(-5, 5) for _ in range(n)], rng.randint(1, n)])(rng.randint(1, 9)),
      brute=r'''
class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]
'''),

    P(65, "Task Scheduler", "Medium", "leastInterval",
      r'''
A CPU must run the tasks in `tasks`, each labelled with an uppercase letter. One task takes one unit of time, and in each unit the CPU either runs a task or sits idle. Tasks may be run in any order.

Between two runs of the same letter there must be at least `n` units in which that letter does not run (the CPU may run other tasks or idle in those units).

Return the minimum number of time units needed to finish every task.

## Examples

```
Input:  tasks = ["X", "X", "Y", "Y"], n = 2
Output: 5          # X Y _ X Y

Input:  tasks = ["A", "A", "A", "B", "B", "B"], n = 3
Output: 10         # A B _ _ A B _ _ A B
```

## Constraints

- `1 <= len(tasks) <= 10000`
- `0 <= n <= 100`
- Tasks are uppercase English letters.

## Hints

- The most frequent task decides the skeleton of the schedule. Other tasks fill its gaps.
- You can count the answer with a formula, or simulate with a max-heap.
''',
      r'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass
''',
      r'''
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        top = max(counts.values())
        ties = sum(1 for c in counts.values() if c == top)
        return max(len(tasks), (top - 1) * (n + 1) + ties)
''',
      [([["X", "X", "Y", "Y"], 2], 5), ([["A", "A", "A", "B", "B", "B"], 3], 10),
       ([["A", "A", "A", "B", "B", "B"], 0], 6), ([["A", "A", "A", "A", "B", "C", "D", "E"], 2], 10),
       ([["A"], 5], 1), ([["A", "B", "C"], 2], 3), ([["A", "A", "A", "B", "B", "C", "C"], 2], 7),
       ([["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2], 12)],
      gen=lambda rng: [_sched(rng, rng.randint(1, 14), "ABCD", rng.randint(0, 3)) for _ in range(6)]
      + [_sched(rng, 10000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 100), _sched(rng, 10000, "AB", 50)],
      small=lambda rng: _sched(rng, rng.randint(1, 9), "ABC", rng.randint(0, 3)),
      brute=r'''
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        left = Counter(tasks)
        last = {}
        t = 0
        while sum(left.values()):
            ready = [c for c, k in left.items() if k and last.get(c, -n - 1) + n < t]
            if ready:
                c = max(ready, key=lambda c: left[c])
                left[c] -= 1
                last[c] = t
            t += 1
        return t
'''),

    P(66, "Design Twitter", "Medium", "Twitter",
      r'''
Design a simplified Twitter. Users post tweets, follow and unfollow each other, and see a news feed.

Implement `Twitter`:

- `Twitter()` creates an empty system.
- `postTweet(userId, tweetId)` makes `userId` post a tweet with the unique id `tweetId`.
- `getNewsFeed(userId)` returns the ids of the 10 most recent tweets in the user's feed, most recent first. The feed contains the user's own tweets and the tweets of everyone they follow.
- `follow(followerId, followeeId)` makes `followerId` start following `followeeId`.
- `unfollow(followerId, followeeId)` makes `followerId` stop following `followeeId`.

## Examples

```
postTweet(1, 5)
getNewsFeed(1)   -> [5]
follow(1, 2)
postTweet(2, 6)
getNewsFeed(1)   -> [6, 5]
unfollow(1, 2)
getNewsFeed(1)   -> [5]
```

## Constraints

- `1 <= userId, followerId, followeeId <= 500`
- `0 <= tweetId <= 10^4`, tweet ids are unique
- `followerId != followeeId`
- At most `10000` calls are made.

## Hints

- Give every tweet an increasing timestamp. For the feed, merge each followed user's latest tweets with a heap.
''',
      r'''
class Twitter:

    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
''',
      r'''
import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        people = self.following[userId] | {userId}
        recent = heapq.nlargest(10, (t for u in people for t in self.tweets[u][-10:]))
        return [tweet_id for _, tweet_id in recent]

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
''',
      [([["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
         [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]], [None, None, [5], None, None, [6, 5], None, [5]]),
       ([["Twitter"] + ["postTweet"] * 12 + ["getNewsFeed"], [[]] + [[1, i] for i in range(1, 13)] + [[1]]],
        [None] + [None] * 12 + [[12, 11, 10, 9, 8, 7, 6, 5, 4, 3]]),
       ([["Twitter", "getNewsFeed", "follow", "getNewsFeed", "postTweet", "postTweet", "getNewsFeed"],
         [[], [3], [3, 4], [3], [4, 100], [3, 200], [3]]], [None, [], None, [], None, None, [200, 100]]),
       ([["Twitter", "postTweet", "follow", "unfollow", "unfollow", "getNewsFeed", "getNewsFeed"],
         [[], [1, 9], [2, 1], [2, 1], [2, 1], [2], [1]]], [None, None, None, None, None, [], [9]])],
      design="Twitter",
      gen=lambda rng: [_twitter(rng, m) for m in (20, 60, 200, 3000)],
      small=lambda rng: _twitter(rng, rng.randint(1, 20)),
      brute=r'''
class Twitter:
    def __init__(self):
        self.log = []
        self.follows = set()

    def postTweet(self, userId, tweetId):
        self.log.append((userId, tweetId))

    def getNewsFeed(self, userId):
        feed = [t for u, t in self.log if u == userId or (userId, u) in self.follows]
        return feed[::-1][:10]

    def follow(self, followerId, followeeId):
        self.follows.add((followerId, followeeId))

    def unfollow(self, followerId, followeeId):
        self.follows.discard((followerId, followeeId))
'''),

    P(67, "Find Median from Data Stream", "Hard", "MedianFinder",
      r'''
Design a structure that receives integers one at a time and can report the median of everything received so far. The median is the middle value of the sorted numbers, or the average of the two middle values when the count is even.

Implement `MedianFinder`:

- `MedianFinder()` creates an empty structure.
- `addNum(num)` adds an integer.
- `findMedian()` returns the current median as a float.

`findMedian` is only called after at least one number has been added.

## Examples

```
addNum(1)
findMedian()   -> 1.0
addNum(3)
findMedian()   -> 2.0
addNum(2)
findMedian()   -> 2.0
```

## Constraints

- `-100000 <= num <= 100000`
- At most `10000` calls are made.

## Hints

- Keep the smaller half in a max-heap and the larger half in a min-heap, and keep their sizes within 1 of each other.
''',
      r'''
class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass
''',
      r'''
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2
''',
      [([["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
         [[], [1], [], [3], [], [2], []]], [None, None, 1.0, None, 2.0, None, 2.0]),
       ([["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
         [[], [5], [], [15], [], [1], [], [3], []]], [None, None, 5.0, None, 10.0, None, 5.0, None, 4.0]),
       ([["MedianFinder", "addNum", "addNum", "addNum", "findMedian"], [[], [-1], [-1], [-1], []]],
        [None, None, None, None, -1.0])],
      design="MedianFinder",
      gen=lambda rng: [_median(rng, m) for m in (10, 40, 150, 4000)],
      small=lambda rng: _median(rng, rng.randint(1, 12)),
      brute=r'''
class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num):
        self.nums.append(num)

    def findMedian(self):
        s = sorted(self.nums)
        n = len(s)
        return float(s[n // 2]) if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
'''),
]
