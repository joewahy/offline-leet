from spec import P

CATEGORY = "sliding-window"


def _letters(rng, alphabet, n):
    return "".join(rng.choice(alphabet) for _ in range(n))


def _min_window_gen(rng):
    out = []
    for _ in range(4):
        s = _letters(rng, "abc", rng.randint(5, 15))
        out.append([s, _letters(rng, "abc", rng.randint(1, 4))])
    s = _letters(rng, "abcde", 8000)
    out.append([s, "abcde" * 3])
    out.append([_letters(rng, "ab", 8000), "abc"])
    out.append(["a" * 4000 + "b" + "a" * 4000, "ab"])
    return out


def _perm_gen(rng):
    out = [[_letters(rng, "ab", rng.randint(1, 3)), _letters(rng, "ab", rng.randint(1, 8))] for _ in range(6)]
    p = list("ab" * 1000)
    rng.shuffle(p)
    out.append(["".join(p), "a" * 10000])
    s2 = list(_letters(rng, "abc", 9000))
    s2[4000:6000] = p
    out.append(["".join(p), "".join(s2)])
    return out


PROBLEMS = [
    P(15, "Best Time to Buy and Sell Stock", "Easy", "maxProfit",
      r'''
`prices[i]` is the price of a stock on day `i`. You may buy on one day and sell on a later day, once.

Return the largest profit you can make. If no profit is possible, return `0`.

## Examples

```
Input:  prices = [10, 1, 5, 6, 7, 1]
Output: 6          # buy at 1, sell at 7

Input:  prices = [10, 8, 7, 5, 2]
Output: 0
```

## Constraints

- `1 <= len(prices) <= 10000`
- `0 <= prices[i] <= 1000`

## Hints

- Track the cheapest price seen so far as you scan.
''',
      r'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def maxProfit(self, prices):
        low, best = prices[0], 0
        for p in prices:
            low = min(low, p)
            best = max(best, p - low)
        return best
''',
      [([[10, 1, 5, 6, 7, 1]], 6), ([[10, 8, 7, 5, 2]], 0), ([[7, 1, 5, 3, 6, 4]], 5), ([[1]], 0),
       ([[2, 4, 1]], 2), ([[3, 3, 3]], 0), ([[1, 2]], 1), ([[2, 1, 2, 1, 0, 1, 2]], 2), ([[5, 1, 2, 10]], 9)],
      gen=lambda rng: [[[rng.randint(0, 20) for _ in range(rng.randint(1, 10))]] for _ in range(3)]
      + [[[rng.randint(0, 1000) for _ in range(10000)]]]
      + [[list(range(5000, 0, -1)) + list(range(1, 5001))]],
      small=lambda rng: [[rng.randint(0, 9) for _ in range(rng.randint(1, 9))]],
      brute=r'''
class Solution:
    def maxProfit(self, prices):
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                best = max(best, prices[j] - prices[i])
        return best
'''),

    P(16, "Longest Substring Without Repeating Characters", "Medium", "lengthOfLongestSubstring",
      r'''
Given a string `s`, return the length of the longest contiguous substring in which no character appears more than once.

## Examples

```
Input:  s = "zxyzxyz"
Output: 3          # "zxy"

Input:  s = "xxxx"
Output: 1
```

## Constraints

- `0 <= len(s) <= 10000`
- `s` contains printable ASCII characters (letters, digits, symbols, spaces).

## Hints

- Keep a window `[left, right]`. When a repeat appears, move `left` just past the earlier copy.
''',
      r'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
''',
      r'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}
        left = best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)
        return best
''',
      [(["zxyzxyz"], 3), (["xxxx"], 1), ([""], 0), (["abcabcbb"], 3), (["bbbbb"], 1), (["pwwkew"], 3),
       ([" "], 1), (["dvdf"], 3), (["abba"], 2), (["tmmzuxt"], 5)],
      gen=lambda rng: [["".join(rng.choice("abc") for _ in range(rng.randint(0, 12)))] for _ in range(3)]
      + [["".join(chr(rng.randint(33, 126)) for _ in range(10000))]]
      + [["".join(chr(33 + i % 94) for i in range(10000))]],
      small=lambda rng: ["".join(rng.choice("abcd") for _ in range(rng.randint(0, 10)))],
      brute=r'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        best = 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if len(set(s[i:j])) == j - i:
                    best = max(best, j - i)
        return best
'''),

    P(17, "Longest Repeating Character Replacement", "Medium", "characterReplacement",
      r'''
You are given an uppercase string `s` and an integer `k`. You may change at most `k` characters of `s` into any other uppercase letters.

Return the length of the longest substring that can be made of a single repeated letter using at most `k` changes.

## Examples

```
Input:  s = "XYYX", k = 2
Output: 4          # change the two X into Y

Input:  s = "AAABABB", k = 1
Output: 5
```

## Constraints

- `1 <= len(s) <= 10000`
- `0 <= k <= len(s)`
- `s` consists of uppercase English letters.

## Hints

- A window is fixable when `window length - count of its most common letter <= k`.
''',
      r'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
''',
      r'''
from collections import defaultdict


class Solution:
    def characterReplacement(self, s, k):
        count = defaultdict(int)
        left = best = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
''',
      [(["XYYX", 2], 4), (["AAABABB", 1], 5), (["ABAB", 2], 4), (["A", 0], 1), (["ABC", 0], 1),
       (["AABABBA", 1], 4), (["ABCDE", 1], 2), (["AAAA", 2], 4), (["BAAAB", 2], 5), (["ABBB", 2], 4)],
      gen=lambda rng: [["".join(rng.choice("ABC") for _ in range(rng.randint(1, 12))), rng.randint(0, 4)]
                       for _ in range(4)]
      + [["".join(rng.choice("AB") for _ in range(10000)), 100]]
      + [["".join(rng.choice("ABCDEFGHIJ") for _ in range(10000)), 500]],
      small=lambda rng: ["".join(rng.choice("ABC") for _ in range(rng.randint(1, 9))), rng.randint(0, 4)],
      brute=r'''
from collections import Counter


class Solution:
    def characterReplacement(self, s, k):
        best = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if len(w) - max(Counter(w).values()) <= k:
                    best = max(best, len(w))
        return best
'''),

    P(18, "Permutation in String", "Medium", "checkInclusion",
      r'''
Given two strings `s1` and `s2`, return `True` if some substring of `s2` is a rearrangement of `s1` (same letters, same counts), otherwise `False`.

## Examples

```
Input:  s1 = "abc", s2 = "lecabee"
Output: True       # "cab"

Input:  s1 = "abc", s2 = "lecaabee"
Output: False
```

## Constraints

- `1 <= len(s1), len(s2) <= 10000`
- Both strings consist of lowercase English letters.

## Hints

- Every candidate substring of `s2` has length `len(s1)`. Slide one fixed-size window and update letter counts incrementally.
''',
      r'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass
''',
      r'''
from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        n = len(s1)
        if n > len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[:n])
        if window == need:
            return True
        for i in range(n, len(s2)):
            window[s2[i]] += 1
            out = s2[i - n]
            window[out] -= 1
            if window[out] == 0:
                del window[out]
            if window == need:
                return True
        return False
''',
      [(["abc", "lecabee"], True), (["abc", "lecaabee"], False), (["ab", "eidbaooo"], True),
       (["ab", "eidboaoo"], False), (["a", "a"], True), (["a", "b"], False), (["abc", "ab"], False),
       (["adc", "dcda"], True), (["hello", "ooolleoooleh"], False), (["ab", "ba"], True)],
      gen=_perm_gen,
      small=lambda rng: [_letters(rng, "ab", rng.randint(1, 3)), _letters(rng, "ab", rng.randint(1, 8))],
      brute=r'''
class Solution:
    def checkInclusion(self, s1, s2):
        n = len(s1)
        return any(sorted(s2[i:i + n]) == sorted(s1) for i in range(len(s2) - n + 1))
'''),

    P(19, "Minimum Window Substring", "Hard", "minWindow",
      r'''
Given strings `s` and `t`, return the shortest substring of `s` that contains every character of `t`, counting repeats (if `t` has two `a`, the window needs two `a`).

If no such substring exists, return `""`. If several windows tie for the shortest length, any one of them is accepted.

## Examples

```
Input:  s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"

Input:  s = "x", t = "xy"
Output: ""
```

## Constraints

- `1 <= len(s), len(t) <= 10000`
- `s` and `t` consist of uppercase and lowercase English letters.

## Hints

- Expand the right edge until the window is valid, then shrink from the left while it stays valid.
''',
      r'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass
''',
      r'''
from collections import Counter


class Solution:
    def minWindow(self, s, t):
        need = Counter(t)
        missing = len(t)
        left = 0
        best = (0, float("inf"))
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left < best[1] - best[0]:
                    best = (left, right)
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return "" if best[1] == float("inf") else s[best[0]:best[1] + 1]
''',
      [(["OUZODYXAZV", "XYZ"], "YXAZ"), (["xyz", "xyz"], "xyz"), (["x", "xy"], ""),
       (["ADOBECODEBANC", "ABC"], "BANC"), (["a", "a"], "a"), (["a", "aa"], ""), (["aa", "aa"], "aa"),
       (["abc", "b"], "b"), (["bba", "ab"], "ba"), (["ab", "b"], "b")],
      checker=r'''
from collections import Counter


def check(args, got, expected, inputs):
    s, t = args
    if not isinstance(got, str):
        return "return a string"
    if expected == "":
        return got == "" or "no valid window exists, expected an empty string"
    if len(got) != len(expected):
        return f"window length {len(got)} is not the minimum ({len(expected)})"
    if got not in s:
        return "result is not a substring of s"
    if Counter(t) - Counter(got):
        return "result does not contain every character of t"
    return True
''',
      gen=_min_window_gen,
      small=lambda rng: [_letters(rng, "abc", rng.randint(1, 9)), _letters(rng, "abc", rng.randint(1, 4))],
      brute=r'''
from collections import Counter


class Solution:
    def minWindow(self, s, t):
        best = ""
        for i in range(len(s)):
            for j in range(i + len(t), len(s) + 1):
                if not (Counter(t) - Counter(s[i:j])) and (best == "" or j - i < len(best)):
                    best = s[i:j]
        return best
'''),

    P(20, "Sliding Window Maximum", "Hard", "maxSlidingWindow",
      r'''
A window of size `k` slides from the left end of `nums` to the right end, one position at a time. Return a list holding the maximum value inside the window at each position.

## Examples

```
Input:  nums = [1, 2, 1, 0, 4, 2, 6], k = 3
Output: [2, 2, 4, 4, 6]

Input:  nums = [9, 11], k = 2
Output: [11]
```

## Constraints

- `1 <= k <= len(nums) <= 10000`
- `-10000 <= nums[i] <= 10000`

## Hints

- A deque of indices, kept in decreasing order of value, gives each maximum in amortised O(1).
''',
      r'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass
''',
      r'''
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        out = []
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                out.append(nums[q[0]])
        return out
''',
      [([[1, 2, 1, 0, 4, 2, 6], 3], [2, 2, 4, 4, 6]), ([[1, 3, -1, -3, 5, 3, 6, 7], 3], [3, 3, 5, 5, 6, 7]),
       ([[1], 1], [1]), ([[9, 11], 2], [11]), ([[4, 3, 2, 1], 2], [4, 3, 2]), ([[1, 2, 3, 4], 2], [2, 3, 4]),
       ([[1, -1], 1], [1, -1]), ([[7, 7, 7], 3], [7]), ([[5, 3, 4], 2], [5, 4])],
      gen=lambda rng: [[[rng.randint(-5, 5) for _ in range(n)], rng.randint(1, n)]
                       for n in (6, 9, 12, 15)]
      + [[[rng.randint(-10000, 10000) for _ in range(10000)], 3000]]
      + [[list(range(10000, 0, -1)), 5000]],
      small=lambda rng: (lambda n: [[rng.randint(-6, 6) for _ in range(n)], rng.randint(1, n)])(rng.randint(1, 9)),
      brute=r'''
class Solution:
    def maxSlidingWindow(self, nums, k):
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]
'''),
]
