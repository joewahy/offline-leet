from spec import P

CATEGORY = "1d-dp"


def _ints(rng, n, lo, hi):
    return [rng.randint(lo, hi) for _ in range(n)]


def _word(rng, n, letters):
    return "".join(rng.choice(letters) for _ in range(n))


def _digits(rng, n):
    return "".join(rng.choice("0111222345678910") for _ in range(n))


def _coins(rng):
    coins = rng.sample(range(1, 30), rng.randint(1, 4))
    return [coins, rng.randint(0, 60)]


def _wb(rng, n_words):
    words = sorted({_word(rng, rng.randint(1, 3), "ab") for _ in range(n_words)})
    s = _word(rng, rng.randint(1, 10), "ab")
    return [s, words]


def _wb_yes(rng):
    words = sorted({_word(rng, rng.randint(1, 4), "abc") for _ in range(rng.randint(2, 5))})
    s = "".join(rng.choice(words) for _ in range(rng.randint(2, 8)))
    return [s, words]


PROBLEMS = [
    P(99, "Climbing Stairs", "Easy", "climbStairs",
      r'''
You are climbing a staircase with `n` steps. Each move you can climb either 1 or 2 steps.

Return the number of distinct sequences of moves that take you exactly to the top.

## Examples

```
Input:  n = 2
Output: 2          # 1+1, 2

Input:  n = 3
Output: 3          # 1+1+1, 1+2, 2+1
```

## Constraints

- `1 <= n <= 45`

## Hints

- The number of ways to reach step `i` is the number of ways to reach `i - 1` plus the number of ways to reach `i - 2`.
''',
      r'''
class Solution:
    def climbStairs(self, n: int) -> int:
        pass
''',
      r'''
class Solution:
    def climbStairs(self, n):
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
''',
      [([1], 1), ([2], 2), ([3], 3), ([4], 5), ([5], 8), ([10], 89), ([20], 10946), ([45], 1836311903)],
      gen=lambda rng: [[n] for n in (6, 12, 30, 40, 44)],
      small=lambda rng: [rng.randint(1, 14)],
      brute=r'''
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
'''),

    P(100, "Min Cost Climbing Stairs", "Easy", "minCostClimbingStairs",
      r'''
`cost[i]` is the price you pay to step off stair `i`. After paying you may move up one or two stairs. You may start from stair `0` or stair `1`.

Return the minimum total cost to get to the top, which is one position past the last stair.

## Examples

```
Input:  cost = [1, 2, 3]
Output: 2          # start at index 1, pay 2, jump to the top

Input:  cost = [1, 2, 1, 2, 1, 1, 1]
Output: 4
```

## Constraints

- `2 <= len(cost) <= 1000`
- `0 <= cost[i] <= 999`

## Hints

- The cheapest way to stand on stair `i` is `cost[i-1]` or `cost[i-2]` added to the cheapest way to stand on that earlier stair.
''',
      r'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def minCostClimbingStairs(self, cost):
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b
''',
      [([[1, 2, 3]], 2), ([[1, 2, 1, 2, 1, 1, 1]], 4), ([[10, 15, 20]], 15), ([[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]], 6),
       ([[0, 0]], 0), ([[5, 5]], 5), ([[1, 2]], 1), ([[2, 2, 1, 100]], 3)],
      gen=lambda rng: [[_ints(rng, n, 0, 20)] for n in (3, 6, 9)] + [[_ints(rng, 1000, 0, 999)], [[999] * 1000]],
      small=lambda rng: [_ints(rng, rng.randint(2, 11), 0, 9)],
      brute=r'''
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)

        def from_pos(i):
            if i >= n:
                return 0
            return cost[i] + min(from_pos(i + 1), from_pos(i + 2))

        return min(from_pos(0), from_pos(1))
'''),

    P(101, "House Robber", "Medium", "rob",
      r'''
`nums[i]` is the amount of money in house `i`, along a street. Houses next to each other have linked alarms: robbing two neighbouring houses sets off the alarm.

Return the largest amount of money you can rob without triggering any alarm.

## Examples

```
Input:  nums = [1, 1, 3, 3]
Output: 4          # rob house 1 and house 3

Input:  nums = [2, 9, 8, 3, 6]
Output: 16         # 2 + 8 + 6
```

## Constraints

- `1 <= len(nums) <= 10000`
- `0 <= nums[i] <= 400`

## Hints

- For each house, either skip it (best so far) or rob it (its money plus the best up to two houses back).
''',
      r'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def rob(self, nums):
        skip, take = 0, 0
        for x in nums:
            skip, take = max(skip, take), skip + x
        return max(skip, take)
''',
      [([[1, 1, 3, 3]], 4), ([[2, 9, 8, 3, 6]], 16), ([[7]], 7), ([[2, 1]], 2), ([[1, 2, 3, 1]], 4),
       ([[2, 7, 9, 3, 1]], 12), ([[0, 0]], 0), ([[5, 5, 5]], 10), ([[100, 1, 1, 100]], 200)],
      gen=lambda rng: [[_ints(rng, n, 0, 40)] for n in (3, 8, 15)] + [[_ints(rng, 10000, 0, 400)]],
      small=lambda rng: [_ints(rng, rng.randint(1, 11), 0, 20)],
      brute=r'''
class Solution:
    def rob(self, nums):
        best = 0
        n = len(nums)
        for mask in range(1 << n):
            if mask & (mask >> 1):
                continue
            best = max(best, sum(nums[i] for i in range(n) if mask >> i & 1))
        return best
'''),

    P(102, "House Robber II", "Medium", "rob",
      r'''
Same as House Robber, but the houses are arranged in a circle: the first and the last house are neighbours. Robbing two neighbouring houses sets off the alarm.

Return the largest amount of money you can rob without triggering any alarm.

## Examples

```
Input:  nums = [3, 4, 3]
Output: 4

Input:  nums = [2, 9, 8, 3, 6]
Output: 15         # 9 + 6
```

## Constraints

- `1 <= len(nums) <= 1000`
- `0 <= nums[i] <= 1000`

## Hints

- Because house 0 and the last house cannot both be robbed, solve the linear problem twice: once without the first house, once without the last.
''',
      r'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def rob(self, nums):
        def line(xs):
            skip, take = 0, 0
            for x in xs:
                skip, take = max(skip, take), skip + x
            return max(skip, take)

        if len(nums) == 1:
            return nums[0]
        return max(line(nums[1:]), line(nums[:-1]))
''',
      [([[3, 4, 3]], 4), ([[2, 9, 8, 3, 6]], 15), ([[1]], 1), ([[1, 2]], 2), ([[1, 2, 3]], 3), ([[1, 2, 3, 1]], 4),
       ([[2, 3, 2]], 3), ([[200, 3, 140, 20, 10]], 340), ([[0]], 0)],
      gen=lambda rng: [[_ints(rng, n, 0, 40)] for n in (2, 4, 8, 15)] + [[_ints(rng, 1000, 0, 1000)]],
      small=lambda rng: [_ints(rng, rng.randint(1, 11), 0, 20)],
      brute=r'''
class Solution:
    def rob(self, nums):
        n = len(nums)
        best = 0
        for mask in range(1 << n):
            if mask & (mask >> 1) or (n > 1 and mask & 1 and mask >> (n - 1) & 1):
                continue
            best = max(best, sum(nums[i] for i in range(n) if mask >> i & 1))
        return best
'''),

    P(103, "Longest Palindromic Substring", "Medium", "longestPalindrome",
      r'''
Given a string `s`, return its longest palindromic substring (a contiguous part of `s` that reads the same forwards and backwards). If several have the same maximum length, any one of them is accepted.

## Examples

```
Input:  s = "ababd"
Output: "bab"      # "aba" is also accepted

Input:  s = "abbc"
Output: "bb"
```

## Constraints

- `1 <= len(s) <= 1000`
- `s` consists of digits and English letters.

## Hints

- Every palindrome has a centre (a character or the gap between two). Expand outwards from each centre.
''',
      r'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass
''',
      r'''
class Solution:
    def longestPalindrome(self, s):
        best = ""
        for centre in range(2 * len(s) - 1):
            lo, hi = centre // 2, centre // 2 + centre % 2
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > len(best):
                best = s[lo + 1:hi]
        return best
''',
      [(["ababd"], "bab"), (["abbc"], "bb"), (["a"], "a"), (["cbbd"], "bb"), (["babad"], "bab"),
       (["racecar"], "racecar"), (["abc"], "a"), (["aaaa"], "aaaa"), (["forgeeksskeegfor"], "geeksskeeg")],
      checker=r'''
def check(args, got, expected, inputs):
    s = args[0]
    if not isinstance(got, str):
        return "return a string"
    if got not in s:
        return "result is not a substring of s"
    if got != got[::-1]:
        return "result is not a palindrome"
    if len(got) != len(expected):
        return f"a palindrome of length {len(expected)} exists, yours has length {len(got)}"
    return True
''',
      gen=lambda rng: [[_word(rng, n, "ab")] for n in (5, 12, 40)] + [[_word(rng, 1000, "ab")], ["a" * 1000], [_word(rng, 1000, "abcdefg")]],
      small=lambda rng: [_word(rng, rng.randint(1, 9), "ab")],
      brute=r'''
class Solution:
    def longestPalindrome(self, s):
        best = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                t = s[i:j + 1]
                if t == t[::-1] and len(t) > len(best):
                    best = t
        return best
'''),

    P(104, "Palindromic Substrings", "Medium", "countSubstrings",
      r'''
Return the number of palindromic substrings of `s`. Substrings at different positions count separately, even if they have the same text.

## Examples

```
Input:  s = "abc"
Output: 3          # "a", "b", "c"

Input:  s = "aaa"
Output: 6          # "a" x3, "aa" x2, "aaa"
```

## Constraints

- `1 <= len(s) <= 1000`
- `s` consists of lowercase English letters.

## Hints

- Expand around each of the `2n - 1` possible centres and count every palindrome you pass.
''',
      r'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        pass
''',
      r'''
class Solution:
    def countSubstrings(self, s):
        count = 0
        for centre in range(2 * len(s) - 1):
            lo, hi = centre // 2, centre // 2 + centre % 2
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1
        return count
''',
      [(["abc"], 3), (["aaa"], 6), (["a"], 1), (["aa"], 3), (["abba"], 6), (["racecar"], 10), (["abab"], 6)],
      gen=lambda rng: [[_word(rng, n, "ab")] for n in (5, 12, 40)] + [[_word(rng, 1000, "ab")], ["a" * 1000]],
      small=lambda rng: [_word(rng, rng.randint(1, 10), "abc")],
      brute=r'''
class Solution:
    def countSubstrings(self, s):
        return sum(s[i:j] == s[i:j][::-1] for i in range(len(s)) for j in range(i + 1, len(s) + 1))
'''),

    P(105, "Decode Ways", "Medium", "numDecodings",
      r'''
A message made of capital letters is encoded as digits using `A -> "1"`, `B -> "2"`, ..., `Z -> "26"`. To decode a digit string, split it into groups that are each a valid code (`"1"` to `"26"`, with no leading zero), and map each group back to a letter.

For example `"11106"` can be decoded as `"AAJF"` (`1 1 10 6`) or `"KJF"` (`11 10 6`), but not as `1 1 1 06`, because `"06"` is not valid.

Return the number of different ways to decode `s`. If there are none, return `0`.

## Examples

```
Input:  s = "12"
Output: 2          # "AB" or "L"

Input:  s = "06"
Output: 0
```

## Constraints

- `1 <= len(s) <= 45`
- `s` contains only digits and may start with `0`.
- The answer fits in a 32-bit integer.

## Hints

- At each position you can use one digit (if it is not `0`) or two digits (if they form 10 to 26). Add up the ways for the rest of the string.
''',
      r'''
class Solution:
    def numDecodings(self, s: str) -> int:
        pass
''',
      r'''
class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
                if i + 1 < n and s[i:i + 2] <= "26":
                    dp[i] += dp[i + 2]
        return dp[0]
''',
      [(["12"], 2), (["226"], 3), (["06"], 0), (["0"], 0), (["1"], 1), (["10"], 1), (["27"], 1), (["100"], 0),
       (["11106"], 2), (["2101"], 1), (["1201234"], 3), (["999"], 1)],
      gen=lambda rng: [[_digits(rng, n)] for n in (4, 8, 12, 20, 30)] + [["1" * 40], ["12" * 20], ["2" * 44 + "6"]],
      small=lambda rng: [_digits(rng, rng.randint(1, 10))],
      brute=r'''
class Solution:
    def numDecodings(self, s):
        if not s:
            return 1
        total = 0
        if s[0] != "0":
            total += self.numDecodings(s[1:])
            if len(s) > 1 and s[:2] <= "26":
                total += self.numDecodings(s[2:])
        return total
'''),

    P(106, "Coin Change", "Medium", "coinChange",
      r'''
`coins` lists the denominations you have (each in unlimited supply) and `amount` is a target sum.

Return the fewest coins that add up to exactly `amount`. If it cannot be made, return `-1`. An amount of `0` needs `0` coins.

## Examples

```
Input:  coins = [1, 5, 10], amount = 12
Output: 3          # 10 + 1 + 1

Input:  coins = [2], amount = 3
Output: -1
```

## Constraints

- `1 <= len(coins) <= 12`
- `1 <= coins[i] <= 10000`, all distinct
- `0 <= amount <= 10000`

## Hints

- `fewest(a) = 1 + min(fewest(a - c))` over the coins `c <= a`. Build the table from `0` upwards.
- A greedy "largest coin first" approach does not always work.
''',
      r'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass
''',
      r'''
class Solution:
    def coinChange(self, coins, amount):
        inf = float("inf")
        dp = [0] + [inf] * amount
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1
        return -1 if dp[amount] == inf else dp[amount]
''',
      [([[1, 5, 10], 12], 3), ([[2], 3], -1), ([[1], 0], 0), ([[1, 2, 5], 11], 3), ([[2], 1], -1),
       ([[186, 419, 83, 408], 6249], 20), ([[3, 7, 405, 436], 8839], 25), ([[1, 3, 4], 6], 2)],
      gen=lambda rng: [_coins(rng) for _ in range(5)]
      + [[[1, 5, 10, 25, 50, 100], 9999], [[7, 13, 29, 101, 997], 10000], [[2, 4, 6, 8], 9999], [[186, 419, 83, 408], 9999]],
      small=lambda rng: _coins(rng),
      brute=r'''
from collections import deque


class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        seen, q = {0}, deque([(0, 0)])
        while q:
            total, used = q.popleft()
            for c in coins:
                if total + c == amount:
                    return used + 1
                if total + c < amount and total + c not in seen:
                    seen.add(total + c)
                    q.append((total + c, used + 1))
        return -1
'''),

    P(107, "Maximum Product Subarray", "Medium", "maxProduct",
      r'''
Given an integer list `nums`, return the largest product of any non-empty contiguous subarray.

## Examples

```
Input:  nums = [1, 2, -3, 4]
Output: 4

Input:  nums = [-2, 3, -4]
Output: 24
```

## Constraints

- `1 <= len(nums) <= 1000`
- `-10 <= nums[i] <= 10`
- The answer fits in a 32-bit integer for the checked tests.

## Hints

- A negative number can turn the smallest product into the largest. Track both the maximum and the minimum product ending at each position.
''',
      r'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def maxProduct(self, nums):
        best = hi = lo = nums[0]
        for x in nums[1:]:
            hi, lo = max(x, hi * x, lo * x), min(x, hi * x, lo * x)
            best = max(best, hi)
        return best
''',
      [([[1, 2, -3, 4]], 4), ([[-2, -1]], 2), ([[2, 3, -2, 4]], 6), ([[-2, 0, -1]], 0), ([[-2]], -2), ([[0]], 0),
       ([[-2, 3, -4]], 24), ([[2, -5, -2, -4, 3]], 24), ([[-1, -1, -1]], 1), ([[3, -1, 4]], 4)],
      gen=lambda rng: [[_ints(rng, n, -3, 3)] for n in (3, 6, 10, 15)]
      + [[_ints(rng, 25, -2, 2)], [[1, -1] * 15], [_ints(rng, 1000, -1, 1)]],
      small=lambda rng: [_ints(rng, rng.randint(1, 9), -3, 3)],
      brute=r'''
class Solution:
    def maxProduct(self, nums):
        best = nums[0]
        for i in range(len(nums)):
            p = 1
            for j in range(i, len(nums)):
                p *= nums[j]
                best = max(best, p)
        return best
'''),

    P(108, "Word Break", "Medium", "wordBreak",
      r'''
Given a string `s` and a list of words `wordDict`, return `True` if `s` can be split into a sequence of one or more dictionary words (words may be reused any number of times), otherwise `False`.

## Examples

```
Input:  s = "neetcode", wordDict = ["neet", "code"]
Output: True

Input:  s = "catsincars", wordDict = ["cats", "cat", "sin", "in", "car"]
Output: False
```

## Constraints

- `1 <= len(s) <= 300`
- `1 <= len(wordDict) <= 1000`, `1 <= len(word) <= 20`
- All strings use lowercase letters; the words in `wordDict` are distinct.

## Hints

- `can[i]` means the first `i` letters can be split. It is true when some `j < i` has `can[j]` and `s[j:i]` is a word.
''',
      r'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass
''',
      r'''
class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        longest = max(map(len, words))
        can = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - longest), i):
                if can[j] and s[j:i] in words:
                    can[i] = True
                    break
        return can[-1]
''',
      [(["neetcode", ["neet", "code"]], True), (["applepenapple", ["apple", "pen"]], True),
       (["catsincars", ["cats", "cat", "sin", "in", "car"]], False), (["leetcode", ["leet", "code"]], True),
       (["catsandog", ["cats", "dog", "sand", "and", "cat"]], False), (["a", ["a"]], True), (["ab", ["a"]], False),
       (["aaaaaaa", ["aaaa", "aaa"]], True), (["aaaaab", ["a", "aa"]], False)],
      gen=lambda rng: [_wb(rng, 3) for _ in range(3)] + [_wb_yes(rng) for _ in range(3)]
      + [["a" * 60 + "b", ["a", "aa", "aaa", "aaaa"]], ["a" * 299, ["a" * 2, "a" * 3, "a" * 5]],
         ["ab" * 100, ["a", "b", "ab", "ba"]]],
      small=lambda rng: _wb(rng, rng.randint(1, 4)),
      brute=r'''
from functools import lru_cache


class Solution:
    def wordBreak(self, s, wordDict):
        @lru_cache(None)
        def go(i):
            return i == len(s) or any(s.startswith(w, i) and go(i + len(w)) for w in wordDict)

        return go(0)
'''),

    P(109, "Longest Increasing Subsequence", "Medium", "lengthOfLIS",
      r'''
Return the length of the longest strictly increasing subsequence of `nums`. A subsequence keeps the original order but may skip elements.

## Examples

```
Input:  nums = [9, 1, 4, 2, 3, 3, 7]
Output: 4          # 1, 2, 3, 7

Input:  nums = [0, 3, 1, 3, 2, 3]
Output: 4
```

## Constraints

- `1 <= len(nums) <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Hints

- `O(n^2)`: for each element, look at every earlier smaller element.
- `O(n log n)`: keep the smallest possible tail of an increasing subsequence of each length, and binary search into it.
''',
      r'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass
''',
      r'''
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums):
        tails = []
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
''',
      [([[9, 1, 4, 2, 3, 3, 7]], 4), ([[0, 3, 1, 3, 2, 3]], 4), ([[10, 9, 2, 5, 3, 7, 101, 18]], 4), ([[7, 7, 7]], 1),
       ([[1]], 1), ([[1, 2, 3, 4]], 4), ([[4, 3, 2, 1]], 1), ([[0, 1, 0, 3, 2, 3]], 4)],
      gen=lambda rng: [[_ints(rng, n, -20, 20)] for n in (4, 8, 15, 30)]
      + [[_ints(rng, 2500, -10000, 10000)], [list(range(2500))], [list(range(2500, 0, -1))]],
      small=lambda rng: [_ints(rng, rng.randint(1, 10), -6, 6)],
      brute=r'''
class Solution:
    def lengthOfLIS(self, nums):
        def go(i, last):
            if i == len(nums):
                return 0
            best = go(i + 1, last)
            if last is None or nums[i] > last:
                best = max(best, 1 + go(i + 1, nums[i]))
            return best

        return go(0, None)
'''),

    P(110, "Partition Equal Subset Sum", "Medium", "canPartition",
      r'''
Given a list of positive integers `nums`, return `True` if it can be split into two groups with exactly the same sum, otherwise `False`. Every number must go into exactly one group.

## Examples

```
Input:  nums = [1, 2, 3, 4]
Output: True       # [1, 4] and [2, 3]

Input:  nums = [1, 2, 3, 5]
Output: False
```

## Constraints

- `1 <= len(nums) <= 100`
- `1 <= nums[i] <= 100`

## Hints

- If the total is odd, it is impossible. Otherwise ask: can some subset add up to `total / 2`?
- Track the set of reachable sums as you go through the numbers.
''',
      r'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass
''',
      r'''
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        reach = 1
        for x in nums:
            reach |= reach << x
        return bool(reach >> (total // 2) & 1)
''',
      [([[1, 2, 3, 4]], True), ([[1, 2, 3, 4, 5]], False), ([[1, 5, 11, 5]], True), ([[1, 2, 3, 5]], False),
       ([[2, 2, 3, 5]], False), ([[100]], False), ([[1, 1]], True), ([[3, 3, 3, 3]], True)],
      gen=lambda rng: [[_ints(rng, n, 1, 12)] for n in (3, 6, 9, 14)]
      + [[_ints(rng, 100, 1, 100)], [[99] * 99 + [98, 1]], [[100] * 100], [[2] * 99 + [1]]],
      small=lambda rng: [_ints(rng, rng.randint(1, 10), 1, 9)],
      brute=r'''
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        n = len(nums)
        return total % 2 == 0 and any(
            sum(nums[i] for i in range(n) if mask >> i & 1) * 2 == total for mask in range(1 << n)
        )
'''),
]
