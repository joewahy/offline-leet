from spec import P

CATEGORY = "binary-search"


def _sorted_search(rng):
    out = []
    for n in (1, 6, 25):
        nums = sorted(rng.sample(range(-100, 100), n))
        out.append([nums, rng.choice(nums)])
        out.append([nums, 1000])
    nums = sorted(rng.sample(range(-100000, 100000), 10000))
    out += [[nums, nums[-2]], [nums, nums[4321]], [nums, 3]]
    return out


def _matrix(rng, rows, cols):
    vals = sorted(rng.sample(range(rows * cols * 3), rows * cols))
    m = [vals[r * cols:(r + 1) * cols] for r in range(rows)]
    return m, vals


def _matrix_gen(rng):
    out = []
    for rows, cols in ((1, 1), (1, 5), (4, 1), (3, 4), (5, 6), (100, 100)):
        m, vals = _matrix(rng, rows, cols)
        out.append([m, rng.choice(vals)])
        out.append([m, vals[-1] + 1])
        out.append([m, vals[0] - 1])
    return out


def _koko(rng, n, pmax, slack):
    piles = [rng.randint(1, pmax) for _ in range(n)]
    return [piles, n + rng.randint(0, slack)]


def _rotated(rng, n, lo=-1000, hi=1000):
    nums = sorted(rng.sample(range(lo, hi), n))
    k = rng.randrange(n)
    return nums[k:] + nums[:k]


def _rot_search(rng):
    out = []
    for n in (1, 2, 5, 12):
        nums = _rotated(rng, n)
        out += [[nums, rng.choice(nums)], [nums, 5000]]
    nums = _rotated(rng, 10000, -100000, 100000)
    out += [[nums, nums[7777]], [nums, nums[0]], [nums, 123456]]
    return out


def _timemap(rng, n):
    ops, params, ts = ["TimeMap"], [[]], 0
    for _ in range(n):
        key = rng.choice("abc")
        if rng.random() < 0.5:
            ts += rng.randint(1, 3)
            ops.append("set")
            params.append([key, "".join(rng.choice("xyz") for _ in range(3)), ts])
        else:
            ops.append("get")
            params.append([key, rng.randint(0, ts + 2)])
    return [ops, params]


def _median_gen(rng):
    out = []
    for a, b in ((0, 1), (1, 0), (3, 3), (2, 7), (8, 1), (5, 5)):
        out.append([sorted(rng.randint(-20, 20) for _ in range(a)), sorted(rng.randint(-20, 20) for _ in range(b))])
    out.append([sorted(rng.randint(-10**6, 10**6) for _ in range(10000)),
                sorted(rng.randint(-10**6, 10**6) for _ in range(9000))])
    return out


PROBLEMS = [
    P(28, "Binary Search", "Easy", "search",
      r'''
`nums` is a list of distinct integers sorted in ascending order. Return the index of `target` in `nums`, or `-1` if it is not there.

Your solution should run in O(log n) time.

## Examples

```
Input:  nums = [-1, 0, 2, 4, 6, 8], target = 4
Output: 3

Input:  nums = [-1, 0, 2, 4, 6, 8], target = 3
Output: -1
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-10000 <= nums[i], target <= 10000`
- All values in `nums` are distinct.

## Hints

- Compare `target` with the middle element, and discard the half that cannot contain it.
''',
      r'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass
''',
      r'''
class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
''',
      [([[-1, 0, 2, 4, 6, 8], 4], 3), ([[-1, 0, 2, 4, 6, 8], 3], -1), ([[5], 5], 0), ([[5], -5], -1),
       ([[1, 2], 2], 1), ([[1, 2], 1], 0), ([[1, 3, 5, 7, 9], 9], 4), ([[1, 3, 5, 7, 9], 0], -1),
       ([[2, 4, 6], 10], -1), ([[-10, -5, 0], -10], 0)],
      gen=_sorted_search,
      small=lambda rng: (lambda n: [n, rng.randint(-20, 20)])(sorted(rng.sample(range(-20, 20), rng.randint(1, 8)))),
      brute=r'''
class Solution:
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1
'''),

    P(29, "Search a 2D Matrix", "Medium", "searchMatrix",
      r'''
`matrix` is a grid of integers where every row is sorted in ascending order, and the first number of each row is larger than the last number of the row above.

Return `True` if `target` appears in the matrix, otherwise `False`. Aim for O(log(m * n)) time.

## Examples

```
Input:  matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target = 10
Output: True

Input:  matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target = 15
Output: False
```

## Constraints

- `1 <= rows, cols <= 100`
- `-10000 <= matrix[i][j], target <= 10000`

## Hints

- Read the grid as one long sorted list. Index `k` maps to row `k // cols`, column `k % cols`.
''',
      r'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass
''',
      r'''
class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = matrix[mid // cols][mid % cols]
            if v == target:
                return True
            if v < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
''',
      [([[[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10], True),
       ([[[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15], False), ([[[1]], 1], True), ([[[1]], 2], False),
       ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3], True),
       ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13], False), ([[[1, 3]], 3], True),
       ([[[1], [3]], 3], True), ([[[1], [3]], 2], False), ([[[1, 2], [3, 4]], 0], False)],
      gen=_matrix_gen,
      small=lambda rng: (lambda m: [m[0], rng.randint(-1, 3 * 12)])(_matrix(rng, rng.randint(1, 4), rng.randint(1, 4))),
      brute=r'''
class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)
'''),

    P(30, "Koko Eating Bananas", "Medium", "minEatingSpeed",
      r'''
There are several piles of bananas; `piles[i]` is the size of pile `i`. You have `h` hours. Each hour you choose one pile and eat up to `k` bananas from it. If the pile has fewer than `k` bananas you eat them all and waste the rest of the hour.

Return the smallest integer eating speed `k` that lets you finish every pile within `h` hours.

## Examples

```
Input:  piles = [1, 4, 3, 2], h = 9
Output: 2

Input:  piles = [25, 10, 23, 4], h = 4
Output: 25
```

## Constraints

- `1 <= len(piles) <= 10000`
- `len(piles) <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Hints

- If speed `k` works, so does any larger speed. That means you can binary search on `k`, between 1 and the biggest pile.
- Hours needed at speed `k` is the sum of `ceil(pile / k)`.
''',
      r'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass
''',
      r'''
class Solution:
    def minEatingSpeed(self, piles, h):
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(-(-p // mid) for p in piles) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo
''',
      [([[1, 4, 3, 2], 9], 2), ([[25, 10, 23, 4], 4], 25), ([[3, 6, 7, 11], 8], 4),
       ([[30, 11, 23, 4, 20], 5], 30), ([[30, 11, 23, 4, 20], 6], 23), ([[1], 1], 1),
       ([[1000000000], 2], 500000000), ([[5, 5, 5], 6], 3), ([[2, 2], 2], 2), ([[312884470], 312884469], 2)],
      gen=lambda rng: [_koko(rng, 4, 12, 6) for _ in range(3)]
      + [[[rng.randint(1, 10**9) for _ in range(10000)], 30000]]
      + [[[rng.randint(1, 10**9) for _ in range(5000)], 5000]],
      small=lambda rng: _koko(rng, rng.randint(1, 5), 9, 6),
      brute=r'''
class Solution:
    def minEatingSpeed(self, piles, h):
        k = 1
        while sum(-(-p // k) for p in piles) > h:
            k += 1
        return k
'''),

    P(31, "Find Minimum in Rotated Sorted Array", "Medium", "findMin",
      r'''
A list of distinct integers that was sorted in ascending order has been rotated: some number of elements were moved from the front to the back. For example `[1, 2, 3, 4, 5]` rotated by 2 becomes `[3, 4, 5, 1, 2]`.

Given the rotated list `nums`, return its minimum element in O(log n) time.

## Examples

```
Input:  nums = [3, 4, 5, 6, 1, 2]
Output: 1

Input:  nums = [4, 5, 6, 7]
Output: 4
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-10000 <= nums[i] <= 10000`
- All values are distinct. A rotation of 0 is possible.

## Hints

- Compare the middle element with the last element to see which half contains the drop.
''',
      r'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
''',
      [([[3, 4, 5, 6, 1, 2]], 1), ([[4, 5, 0, 1, 2, 3]], 0), ([[4, 5, 6, 7]], 4), ([[1]], 1), ([[2, 1]], 1),
       ([[1, 2]], 1), ([[5, 1, 2, 3, 4]], 1), ([[2, 3, 4, 5, 1]], 1), ([[3, 1, 2]], 1), ([[11, 13, 15, 17]], 11)],
      gen=lambda rng: [[_rotated(rng, n)] for n in (1, 2, 3, 7, 20)] + [[_rotated(rng, 10000, -10000, 10000)]],
      small=lambda rng: [_rotated(rng, rng.randint(1, 9), -20, 20)],
      brute=r'''
class Solution:
    def findMin(self, nums):
        return min(nums)
'''),

    P(32, "Search in Rotated Sorted Array", "Medium", "search",
      r'''
A list `nums` of distinct integers, originally sorted ascending, has been rotated at an unknown pivot (for example `[0, 1, 2, 4, 5, 6, 7]` may become `[4, 5, 6, 7, 0, 1, 2]`).

Return the index of `target` in `nums`, or `-1` if it is absent. Your solution must run in O(log n) time.

## Examples

```
Input:  nums = [3, 4, 5, 6, 1, 2], target = 1
Output: 4

Input:  nums = [3, 5, 6, 0, 1, 2], target = 4
Output: -1
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-10000 <= nums[i], target <= 10000`
- All values are distinct.

## Hints

- At every step, at least one half of the current range is properly sorted. Check whether the target lies in it.
''',
      r'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass
''',
      r'''
class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
''',
      [([[3, 4, 5, 6, 1, 2], 1], 4), ([[3, 5, 6, 0, 1, 2], 4], -1), ([[4, 5, 6, 7, 0, 1, 2], 0], 4),
       ([[4, 5, 6, 7, 0, 1, 2], 3], -1), ([[1], 0], -1), ([[1], 1], 0), ([[3, 1], 1], 1), ([[3, 1], 3], 0),
       ([[5, 1, 3], 5], 0), ([[5, 1, 3], 3], 2), ([[1, 3], 3], 1)],
      gen=_rot_search,
      small=lambda rng: [_rotated(rng, rng.randint(1, 9), -12, 12), rng.randint(-12, 12)],
      brute=r'''
class Solution:
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1
'''),

    P(33, "Time Based Key-Value Store", "Medium", "TimeMap",
      r'''
Design a key-value store that remembers every value a key has ever had, together with the time it was set.

Implement the class `TimeMap`:

- `TimeMap()` creates an empty store.
- `set(key, value, timestamp)` stores `value` for `key` at `timestamp`.
- `get(key, timestamp)` returns the value that was set for `key` at the largest timestamp that is less than or equal to `timestamp`. If there is no such value, return `""`.

For a given key, `set` is always called with strictly increasing timestamps.

## Examples

```
set("alice", "happy", 1)
get("alice", 1)   -> "happy"
get("alice", 2)   -> "happy"
set("alice", "sad", 3)
get("alice", 3)   -> "sad"
get("alice", 4)   -> "sad"
```

## Constraints

- `1 <= len(key), len(value) <= 100`
- `1 <= timestamp <= 10^7`
- At most `10000` calls are made.

## Hints

- The timestamps of each key are sorted, so `get` can binary search them.
''',
      r'''
class TimeMap:

    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass
''',
      r'''
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.times = {}
        self.values = {}

    def set(self, key, value, timestamp):
        self.times.setdefault(key, []).append(timestamp)
        self.values.setdefault(key, []).append(value)

    def get(self, key, timestamp):
        i = bisect_right(self.times.get(key, []), timestamp)
        return self.values[key][i - 1] if i else ""
''',
      [([["TimeMap", "set", "get", "get", "set", "get", "get"],
         [[], ["alice", "happy", 1], ["alice", 1], ["alice", 2], ["alice", "sad", 3], ["alice", 3], ["alice", 4]]],
        [None, None, "happy", "happy", None, "sad", "sad"]),
       ([["TimeMap", "get", "set", "get", "get"], [[], ["a", 5], ["a", "x", 10], ["a", 9], ["a", 10]]],
        [None, "", None, "", "x"]),
       ([["TimeMap", "set", "set", "set", "get", "get", "get", "get"],
         [[], ["a", "1", 1], ["b", "2", 2], ["a", "3", 3], ["a", 2], ["b", 1], ["b", 5], ["a", 3]]],
        [None, None, None, None, "1", "", "2", "3"]),
       ([["TimeMap", "set", "set", "get", "get", "get"], [[], ["k", "v1", 1], ["k", "v2", 4], ["k", 3], ["k", 4], ["k", 100]]],
        [None, None, None, "v1", "v2", "v2"])],
      design="TimeMap",
      gen=lambda rng: [_timemap(rng, n) for n in (15, 50, 200, 4000)],
      small=lambda rng: _timemap(rng, rng.randint(1, 14)),
      brute=r'''
class TimeMap:
    def __init__(self):
        self.d = {}

    def set(self, key, value, timestamp):
        self.d.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        best = ""
        for t, v in self.d.get(key, []):
            if t <= timestamp:
                best = v
        return best
'''),

    P(34, "Median of Two Sorted Arrays", "Hard", "findMedianSortedArrays",
      r'''
`nums1` and `nums2` are two lists of integers, each sorted in ascending order. Return the median of all their values combined (the middle value, or the average of the two middle values when the total count is even).

Your solution must run in O(log(min(m, n))) time.

## Examples

```
Input:  nums1 = [1, 2], nums2 = [3]
Output: 2.0

Input:  nums1 = [1, 3], nums2 = [2, 4]
Output: 2.5
```

## Constraints

- `0 <= len(nums1), len(nums2) <= 10000`
- `1 <= len(nums1) + len(nums2)`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Hints

- Binary search how many elements of the smaller array belong to the left half of the merged order.
- A split is correct when everything on the left is `<=` everything on the right.
''',
      r'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass
''',
      r'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total = len(a) + len(b)
        half = (total + 1) // 2
        lo, hi = 0, len(a)
        inf = float("inf")
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            a_left = a[i - 1] if i > 0 else -inf
            a_right = a[i] if i < len(a) else inf
            b_left = b[j - 1] if j > 0 else -inf
            b_right = b[j] if j < len(b) else inf
            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            if a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1
''',
      [([[1, 2], [3]], 2.0), ([[1, 3], [2, 4]], 2.5), ([[], [1]], 1.0), ([[2], []], 2.0), ([[0, 0], [0, 0]], 0.0),
       ([[1, 2, 3], [4, 5, 6]], 3.5), ([[1], [2, 3, 4, 5]], 3.0), ([[-5, 3, 6], [-2, 4]], 3.0),
       ([[1, 1], [1, 2, 2]], 1.0)],
      compare="float",
      gen=_median_gen,
      small=lambda rng: (lambda a, b: [sorted(rng.randint(-9, 9) for _ in range(a)), sorted(rng.randint(-9, 9) for _ in range(b))])(
          *rng.choice([(0, 1), (1, 0), (2, 3), (4, 1), (3, 3), (1, 6)])),
      brute=r'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = sorted(nums1 + nums2)
        n = len(m)
        return float(m[n // 2]) if n % 2 else (m[n // 2 - 1] + m[n // 2]) / 2
'''),
]
