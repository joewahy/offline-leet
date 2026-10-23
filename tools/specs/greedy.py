from spec import P

CATEGORY = "greedy"


def _ints(rng, n, lo, hi):
    return [rng.randint(lo, hi) for _ in range(n)]


def _jump_reachable(rng, n, hi):
    return [rng.randint(1, hi) for _ in range(n - 1)] + [rng.randint(0, hi)]


def _gas(rng, n):
    gas = [rng.randint(0, 6) for _ in range(n)]
    cost = [rng.randint(0, 6) for _ in range(n)]
    return [gas, cost]


def _gas_balanced(rng, n):
    gas = [rng.randint(0, 9) for _ in range(n)]
    cost = gas[:]
    rng.shuffle(cost)
    return [gas, cost]


def _hand(rng, groups, size, corrupt):
    hand = []
    for _ in range(groups):
        start = rng.randint(0, 10)
        hand += list(range(start, start + size))
    rng.shuffle(hand)
    if corrupt and hand:
        hand[rng.randrange(len(hand))] += rng.choice([1, 2, 5])
    return [hand, size]


def _hand_gen(rng):
    out = [_hand(rng, g, s, c) for g, s, c in ((2, 3, False), (3, 2, False), (2, 4, True), (4, 2, True), (1, 1, False))]
    out.append([[1, 2, 3, 4], 3])
    out.append(_hand(rng, 2500, 4, False))
    out.append(_hand(rng, 2500, 4, True))
    return out


def _triplets(rng, n):
    target = [rng.randint(1, 6) for _ in range(3)]
    return [[[rng.randint(1, 7) for _ in range(3)] for _ in range(n)], target]


def _labels(rng, n, letters):
    return "".join(rng.choice(letters) for _ in range(n))


def _paren_str(rng, n):
    return "".join(rng.choice("(()))**") for _ in range(n))


def _paren_gen(rng):
    out = [[_paren_str(rng, rng.randint(1, 10))] for _ in range(8)]
    out += [["(" * 50 + "*" * 50 + ")" * 50], ["*" * 100], ["(" * 51 + "*" * 49 + ")" * 50], ["(*" * 40 + ")" * 40 + "*)" * 5]]
    return out


PROBLEMS = [
    P(122, "Maximum Subarray", "Medium", "maxSubArray",
      r'''
Given an integer list `nums`, find the contiguous non-empty subarray with the largest sum and return that sum.

## Examples

```
Input:  nums = [2, -3, 4, -2, 2, 1, -1, 4]
Output: 8          # 4, -2, 2, 1, -1, 4

Input:  nums = [-1]
Output: -1
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-1000 <= nums[i] <= 1000`

## Hints

- If the running sum becomes negative, it can only hurt: start a fresh subarray from the next element.
''',
      r'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def maxSubArray(self, nums):
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best
''',
      [([[2, -3, 4, -2, 2, 1, -1, 4]], 8), ([[-2, 1, -3, 4, -1, 2, 1, -5, 4]], 6), ([[1]], 1), ([[5, 4, -1, 7, 8]], 23),
       ([[-1]], -1), ([[-2, -1]], -1), ([[0, 0]], 0), ([[-3, -2, -1]], -1)],
      gen=lambda rng: [[_ints(rng, n, -10, 10)] for n in (3, 8, 15)] + [[_ints(rng, 10000, -1000, 1000)], [_ints(rng, 10000, -1000, -1)]],
      small=lambda rng: [_ints(rng, rng.randint(1, 10), -8, 8)],
      brute=r'''
class Solution:
    def maxSubArray(self, nums):
        return max(sum(nums[i:j]) for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))
'''),

    P(123, "Jump Game", "Medium", "canJump",
      r'''
You start at the first index of `nums`. `nums[i]` is the maximum number of positions you can jump forward from index `i` (you may also jump less).

Return `True` if you can reach the last index, otherwise `False`.

## Examples

```
Input:  nums = [1, 2, 0, 1, 0]
Output: True

Input:  nums = [1, 2, 1, 0, 1]
Output: False
```

## Constraints

- `1 <= len(nums) <= 10000`
- `0 <= nums[i] <= 1000`

## Hints

- Track the farthest index you can reach so far. If you ever stand on an index beyond it, you are stuck.
''',
      r'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pass
''',
      r'''
class Solution:
    def canJump(self, nums):
        reach = 0
        for i, x in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + x)
        return True
''',
      [([[1, 2, 0, 1, 0]], True), ([[1, 2, 1, 0, 1]], False), ([[0]], True), ([[2, 3, 1, 1, 4]], True),
       ([[3, 2, 1, 0, 4]], False), ([[0, 1]], False), ([[1, 0]], True), ([[2, 0, 0]], True), ([[1, 1, 1, 1]], True)],
      gen=lambda rng: [[_ints(rng, n, 0, 3)] for n in (4, 8, 12, 20)]
      + [[_ints(rng, 10000, 0, 2)], [_ints(rng, 10000, 1, 5)], [[1] * 9999 + [0]], [[1] * 5000 + [0] + [1] * 4999]],
      small=lambda rng: [_ints(rng, rng.randint(1, 9), 0, 3)],
      brute=r'''
class Solution:
    def canJump(self, nums):
        ok = [False] * len(nums)
        ok[0] = True
        for i in range(len(nums)):
            if ok[i]:
                for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                    ok[j] = True
        return ok[-1]
'''),

    P(124, "Jump Game II", "Medium", "jump",
      r'''
You start at index `0` of `nums`. `nums[i]` is the maximum number of positions you can jump forward from index `i`. The last index is always reachable.

Return the minimum number of jumps needed to reach the last index.

## Examples

```
Input:  nums = [2, 4, 1, 1, 1, 1]
Output: 2

Input:  nums = [2, 1, 2, 1, 0]
Output: 2
```

## Constraints

- `1 <= len(nums) <= 10000`
- `0 <= nums[i] <= 100`, and the last index can be reached from index 0

## Hints

- Think in "levels" like a breadth-first search: each jump reaches a window of indices; the next window starts right after it.
''',
      r'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def jump(self, nums):
        jumps = end = far = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                jumps += 1
                end = far
        return jumps
''',
      [([[2, 4, 1, 1, 1, 1]], 2), ([[2, 1, 2, 1, 0]], 2), ([[2, 3, 1, 1, 4]], 2), ([[2, 3, 0, 1, 4]], 2), ([[0]], 0),
       ([[1]], 0), ([[1, 1, 1]], 2), ([[10, 1, 1]], 1)],
      gen=lambda rng: [[_jump_reachable(rng, n, 4)] for n in (4, 8, 12, 20)]
      + [[_jump_reachable(rng, 10000, 10)], [[1] * 9999 + [0]], [_jump_reachable(rng, 10000, 100)]],
      small=lambda rng: [_jump_reachable(rng, rng.randint(1, 10), 4)],
      brute=r'''
class Solution:
    def jump(self, nums):
        inf = float("inf")
        dp = [inf] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
'''),

    P(125, "Gas Station", "Medium", "canCompleteCircuit",
      r'''
There are `n` gas stations on a circular road. Station `i` has `gas[i]` units of fuel, and driving from station `i` to the next one (station `i + 1`, wrapping around) costs `cost[i]` units. Your tank starts empty and is unlimited in size.

Return the index of a station where you can start and drive once around the circle clockwise. If it is impossible, return `-1`. If there is a solution, it is unique.

## Examples

```
Input:  gas = [1, 2, 3, 4], cost = [2, 2, 4, 1]
Output: 3

Input:  gas = [1, 2, 3], cost = [2, 3, 2]
Output: -1
```

## Constraints

- `1 <= n <= 10000`
- `0 <= gas[i], cost[i] <= 1000`

## Hints

- If the total gas is less than the total cost, no start works.
- If you run out of fuel going from `i` to `j`, no station in between can be the start; try `j + 1`.
''',
      r'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start, tank = i + 1, 0
        return start
''',
      [([[1, 2, 3, 4], [2, 2, 4, 1]], 3), ([[1, 2, 3], [2, 3, 2]], -1), ([[2, 3, 4], [3, 4, 3]], -1),
       ([[5, 1, 2, 3, 4], [4, 4, 1, 5, 1]], 4), ([[3, 1, 1], [1, 2, 2]], 0), ([[2], [2]], 0), ([[1], [2]], -1),
       ([[5, 8, 2, 8], [6, 5, 6, 6]], 3)],
      checker=r'''
def check(args, got, expected, inputs):
    gas, cost = args
    if type(got) is not int:
        return "return an integer index"
    if expected == -1:
        return got == -1 or "no starting station works, expected -1"
    if not 0 <= got < len(gas):
        return "the index is out of range"
    tank = 0
    for k in range(len(gas)):
        i = (got + k) % len(gas)
        tank += gas[i] - cost[i]
        if tank < 0:
            return f"you run out of fuel before station {(i + 1) % len(gas)} when starting at {got}"
    return True
''',
      gen=lambda rng: [_gas(rng, n) for n in (3, 5, 8, 12)] + [_gas_balanced(rng, n) for n in (5, 9)]
      + [_gas(rng, 10000), [[1] * 10000, [1] * 10000], [[0] * 9999 + [9], [1] * 9999 + [0]]],
      small=lambda rng: _gas(rng, rng.randint(1, 7)),
      brute=r'''
class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        for start in range(n):
            tank = 0
            for k in range(n):
                i = (start + k) % n
                tank += gas[i] - cost[i]
                if tank < 0:
                    break
            else:
                return start
        return -1
'''),

    P(126, "Hand of Straights", "Medium", "isNStraightHand",
      r'''
`hand[i]` is the number written on the `i`-th card. You want to rearrange all the cards into groups of exactly `groupSize` cards, where the numbers in each group are consecutive (like 4, 5, 6).

Return `True` if this is possible, otherwise `False`.

## Examples

```
Input:  hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
Output: True       # [1,2,3], [2,3,4], [6,7,8]

Input:  hand = [1, 2, 3, 4, 5], groupSize = 4
Output: False
```

## Constraints

- `1 <= len(hand) <= 10000`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= len(hand)`

## Hints

- The smallest remaining card must start a group. Take it and the next `groupSize - 1` consecutive values.
- Count cards with a dictionary, and process the values in sorted order.
''',
      r'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        pass
''',
      r'''
from collections import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for x in sorted(count):
            need = count[x]
            if need:
                for y in range(x, x + groupSize):
                    if count[y] < need:
                        return False
                    count[y] -= need
        return True
''',
      [([[1, 2, 3, 6, 2, 3, 4, 7, 8], 3], True), ([[1, 2, 3, 4, 5], 4], False), ([[1], 1], True), ([[1, 2, 3], 3], True),
       ([[1, 1, 2, 2, 3, 3], 3], True), ([[1, 2, 4], 3], False), ([[5, 6, 7, 8], 2], True), ([[1, 2, 3, 4], 3], False),
       ([[8, 10, 12], 3], False)],
      gen=_hand_gen,
      small=lambda rng: _hand(rng, rng.randint(1, 3), rng.randint(1, 3), rng.random() < 0.4),
      brute=r'''
class Solution:
    def isNStraightHand(self, hand, groupSize):
        cards = sorted(hand)
        if len(cards) % groupSize:
            return False
        while cards:
            first = cards[0]
            for k in range(groupSize):
                if first + k not in cards:
                    return False
                cards.remove(first + k)
        return True
'''),

    P(127, "Merge Triplets to Form Target Triplet", "Medium", "mergeTriplets",
      r'''
`triplets[i] = [a, b, c]` are triples of integers, and `target = [x, y, z]` is the triple you want to build.

You may repeatedly pick two different triplets `i` and `j` and replace `triplets[j]` with `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

Return `True` if, after any number of such operations, `target` appears as one of the triplets, otherwise `False`.

## Examples

```
Input:  triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: True

Input:  triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: False
```

## Constraints

- `1 <= len(triplets) <= 10000`
- `1 <= a, b, c, x, y, z <= 1000`

## Hints

- A triplet with any value larger than the target can never be used. Among the rest, check that each target position gets matched.
''',
      r'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        pass
''',
      r'''
class Solution:
    def mergeTriplets(self, triplets, target):
        got = [0, 0, 0]
        for t in triplets:
            if all(a <= b for a, b in zip(t, target)):
                got = [max(a, b) for a, b in zip(got, t)]
        return got == target
''',
      [([[[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]], True), ([[[3, 4, 5], [4, 5, 6]], [3, 2, 5]], False),
       ([[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]], True), ([[[1, 1, 1]], [1, 1, 1]], True),
       ([[[1, 1, 1]], [2, 1, 1]], False), ([[[2, 2, 2], [1, 3, 1]], [2, 3, 2]], True),
       ([[[3, 1, 1], [1, 1, 3]], [3, 1, 3]], True), ([[[3, 1, 1], [1, 2, 3]], [3, 1, 3]], False)],
      gen=lambda rng: [_triplets(rng, n) for n in (2, 4, 6, 8)] + [_triplets(rng, 10000), [[[1, 1, 1]] * 9999 + [[1000, 1000, 1000]], [1000, 1000, 1000]]],
      small=lambda rng: _triplets(rng, rng.randint(1, 6)),
      brute=r'''
from itertools import combinations


class Solution:
    def mergeTriplets(self, triplets, target):
        for r in range(1, len(triplets) + 1):
            for chosen in combinations(triplets, r):
                if [max(t[i] for t in chosen) for i in range(3)] == target:
                    return True
        return False
'''),

    P(128, "Partition Labels", "Medium", "partitionLabels",
      r'''
Split the string `s` into as many consecutive parts as possible so that each letter appears in at most one part. Return the lengths of the parts, in order.

## Examples

```
Input:  s = "xyxxyzbzbbisl"
Output: [5, 5, 1, 1, 1]

Input:  s = "abcabc"
Output: [6]
```

## Constraints

- `1 <= len(s) <= 10000`
- `s` consists of lowercase English letters.

## Hints

- Record the last position of each letter. Walk through `s`, extending the current part to the farthest last position seen; cut when you reach it.
''',
      r'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pass
''',
      r'''
class Solution:
    def partitionLabels(self, s):
        last = {c: i for i, c in enumerate(s)}
        out, start, end = [], 0, 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                out.append(end - start + 1)
                start = i + 1
        return out
''',
      [(["xyxxyzbzbbisl"], [5, 5, 1, 1, 1]), (["abcabc"], [6]), (["a"], [1]),
       (["ababcbacadefegdehijhklij"], [9, 7, 8]), (["abc"], [1, 1, 1]), (["aaa"], [3]), (["eccbbbbdec"], [10]),
       (["caedbdedda"], [1, 9])],
      gen=lambda rng: [[_labels(rng, n, "abcd")] for n in (5, 10, 20)] + [[_labels(rng, 10000, "abcdefghijklmnopqrstuvwxyz")],
                                                                     [_labels(rng, 10000, "abcdefg")], [("abcdefghijklmnopqrstuvwxyz" * 400)[:10000]]],
      small=lambda rng: [_labels(rng, rng.randint(1, 12), "abcde")],
      brute=r'''
class Solution:
    def partitionLabels(self, s):
        sizes, start = [], 0
        for cut in range(1, len(s) + 1):
            if not set(s[start:cut]) & set(s[cut:]):
                sizes.append(cut - start)
                start = cut
        return sizes
'''),

    P(129, "Valid Parenthesis String", "Medium", "checkValidString",
      r'''
The string `s` contains only `(`, `)` and `*`. The `*` is a wildcard: it may be treated as `(`, as `)`, or as an empty string.

Return `True` if `s` can be made a valid parentheses string, otherwise `False`. A valid string has every `(` matched by a later `)` and every `)` matched by an earlier `(`.

## Examples

```
Input:  s = "((**))"
Output: True

Input:  s = "(((*)"
Output: False
```

## Constraints

- `1 <= len(s) <= 100`
- Each character is `(`, `)` or `*`.

## Hints

- Track the smallest and largest possible number of unmatched `(` as you scan. If the largest goes negative, you have too many `)`; at the end the smallest must be able to reach 0.
''',
      r'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        pass
''',
      r'''
class Solution:
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            if c == "(":
                lo, hi = lo + 1, hi + 1
            elif c == ")":
                lo, hi = lo - 1, hi - 1
            else:
                lo, hi = lo - 1, hi + 1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0
''',
      [(["((**))"], True), (["(((*)"], False), (["(*)"], True), (["(*))"], True), ([")("], False), (["*"], True),
       (["("], False), (["()"], True), (["*)"], True), (["(*"], True), (["**"], True), ([")*"], False), (["(()*"], True)],
      gen=_paren_gen,
      small=lambda rng: [_paren_str(rng, rng.randint(1, 9))],
      brute=r'''
class Solution:
    def checkValidString(self, s):
        def go(i, open_):
            if open_ < 0:
                return False
            if i == len(s):
                return open_ == 0
            c = s[i]
            if c == "(":
                return go(i + 1, open_ + 1)
            if c == ")":
                return go(i + 1, open_ - 1)
            return go(i + 1, open_ + 1) or go(i + 1, open_ - 1) or go(i + 1, open_)

        return go(0, 0)
'''),
]
