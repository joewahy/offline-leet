from spec import P

CATEGORY = "2d-dp"


def _ints(rng, n, lo, hi):
    return [rng.randint(lo, hi) for _ in range(n)]


def _word(rng, n, letters):
    return "".join(rng.choice(letters) for _ in range(n))


def _lcs_gen(rng):
    out = [[_word(rng, rng.randint(1, 8), "abc"), _word(rng, rng.randint(1, 8), "abc")] for _ in range(4)]
    out += [[_word(rng, 1000, "ab"), _word(rng, 1000, "ab")], [_word(rng, 1000, "abcdefghij"), _word(rng, 900, "abcdefghij")]]
    return out


def _interleave(rng, a, b, mutate):
    i = j = 0
    out = []
    while i < len(a) or j < len(b):
        if j >= len(b) or (i < len(a) and rng.random() < 0.5):
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    s3 = "".join(out)
    if mutate and s3:
        k = rng.randrange(len(s3))
        s3 = s3[:k] + rng.choice("abc") + s3[k + 1:]
    return [a, b, s3]


def _interleave_gen(rng):
    out = []
    for la, lb, mut in ((2, 2, False), (3, 3, True), (4, 5, False), (5, 4, True), (0, 3, False), (3, 0, True)):
        out.append(_interleave(rng, _word(rng, la, "ab"), _word(rng, lb, "ab"), mut))
    out.append(_interleave(rng, _word(rng, 100, "ab"), _word(rng, 100, "ab"), False))
    out.append(["a" * 100, "a" * 100, "a" * 199 + "b"])
    out.append(_interleave(rng, _word(rng, 100, "abc"), _word(rng, 99, "abc"), True))
    return out


def _matrix(rng, rows, cols, hi):
    return [[rng.randint(0, hi) for _ in range(cols)] for _ in range(rows)]


def _path_gen(rng):
    out = [[_matrix(rng, r, c, 6)] for r, c in ((1, 1), (1, 4), (3, 3), (4, 5), (6, 6))]
    out.append([[[r * 50 + c for c in range(50)] for r in range(50)]])
    out.append([[[(r * 50 + c) if r % 2 == 0 else (r * 50 + 49 - c) for c in range(50)] for r in range(50)]])
    out.append([_matrix(rng, 50, 50, 5)])
    return out


def _regex(rng, tokens, letters="ab"):
    p = ""
    for _ in range(tokens):
        p += rng.choice(letters + ".") + ("*" if rng.random() < 0.4 else "")
    return p


def _regex_gen(rng):
    out = []
    for _ in range(14):
        out.append([_word(rng, rng.randint(0, 8), "ab"), _regex(rng, rng.randint(0, 5))])
    out.append(["a" * 30, "a*" * 15 + "b"])
    out.append(["a" * 20, "a*a*a*a*a*a*a*a*a*b*"])
    out.append(["ab" * 10, ".*" * 5 + "c"])
    return out


PROBLEMS = [
    P(111, "Unique Paths", "Medium", "uniquePaths",
      r'''
A robot stands in the top-left cell of an `m x n` grid and wants to reach the bottom-right cell. It can only move right or down.

Return the number of different paths the robot can take.

## Examples

```
Input:  m = 3, n = 6
Output: 21

Input:  m = 3, n = 3
Output: 6
```

## Constraints

- `1 <= m, n <= 100`
- The answer fits in a 32-bit integer for the tested sizes.

## Hints

- The number of ways to reach a cell is the number of ways to reach the cell above plus the cell to the left.
- It is also a combinatorics problem: choose which of the `m + n - 2` moves go down.
''',
      r'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass
''',
      r'''
class Solution:
    def uniquePaths(self, m, n):
        row = [1] * n
        for _ in range(m - 1):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]
''',
      [([3, 6], 21), ([3, 3], 6), ([1, 1], 1), ([1, 5], 1), ([2, 2], 2), ([3, 7], 28), ([7, 3], 28), ([10, 10], 48620),
       ([3, 2], 3), ([23, 12], 193536720)],
      gen=lambda rng: [[rng.randint(1, 8), rng.randint(1, 8)] for _ in range(4)] + [[16, 16], [20, 20], [30, 12]],
      small=lambda rng: [rng.randint(1, 6), rng.randint(1, 6)],
      brute=r'''
class Solution:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
'''),

    P(112, "Longest Common Subsequence", "Medium", "longestCommonSubsequence",
      r'''
Return the length of the longest common subsequence of two strings `text1` and `text2`. A subsequence keeps the original order of characters but may skip some. If the strings share nothing, return `0`.

## Examples

```
Input:  text1 = "cat", text2 = "crabt"
Output: 3          # "cat"

Input:  text1 = "abc", text2 = "def"
Output: 0
```

## Constraints

- `1 <= len(text1), len(text2) <= 1000`
- Both strings consist of lowercase English letters.

## Hints

- `dp[i][j]` is the answer for the first `i` letters of `text1` and the first `j` of `text2`. If the last letters match, add 1 to `dp[i-1][j-1]`; otherwise take the better of dropping one letter.
''',
      r'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass
''',
      r'''
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        prev = [0] * (len(text2) + 1)
        for a in text1:
            cur = [0]
            for j, b in enumerate(text2):
                cur.append(prev[j] + 1 if a == b else max(prev[j + 1], cur[j]))
            prev = cur
        return prev[-1]
''',
      [(["cat", "crabt"], 3), (["abcd", "abcd"], 4), (["abc", "def"], 0), (["abcde", "ace"], 3), (["bl", "yby"], 1),
       (["a", "a"], 1), (["oxcpqrsvwf", "shmtulqrypy"], 2)],
      gen=_lcs_gen,
      small=lambda rng: [_word(rng, rng.randint(1, 7), "abc"), _word(rng, rng.randint(1, 7), "abc")],
      brute=r'''
from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        @lru_cache(None)
        def go(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + go(i + 1, j + 1)
            return max(go(i + 1, j), go(i, j + 1))

        return go(0, 0)
'''),

    P(113, "Best Time to Buy and Sell Stock With Cooldown", "Medium", "maxProfit",
      r'''
`prices[i]` is a stock price on day `i`. You may buy and sell as many times as you like, with these rules:

- You can hold at most one share at a time (sell before buying again).
- After you sell, you cannot buy on the very next day (one day of cooldown).

Return the maximum profit.

## Examples

```
Input:  prices = [1, 3, 4, 0, 4]
Output: 6          # buy 1, sell 3, cooldown, buy 0, sell 4

Input:  prices = [1]
Output: 0
```

## Constraints

- `1 <= len(prices) <= 5000`
- `0 <= prices[i] <= 1000`

## Hints

- Track three states per day: holding a share, just sold (in cooldown), and resting with nothing.
''',
      r'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def maxProfit(self, prices):
        hold, sold, rest = float("-inf"), 0, 0
        for p in prices:
            hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
        return max(sold, rest)
''',
      [([[1, 3, 4, 0, 4]], 6), ([[1]], 0), ([[1, 2, 3, 0, 2]], 3), ([[1, 2]], 1), ([[2, 1]], 0), ([[1, 2, 4]], 3),
       ([[6, 1, 6, 4, 3, 0, 2]], 7), ([[1, 4, 2]], 3), ([[1, 2, 3, 4, 5]], 4)],
      gen=lambda rng: [[_ints(rng, n, 0, 10)] for n in (3, 6, 10, 20)] + [[_ints(rng, 5000, 0, 1000)], [list(range(1000)) * 5]],
      small=lambda rng: [_ints(rng, rng.randint(1, 10), 0, 9)],
      brute=r'''
class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        def go(i, holding):
            if i >= n:
                return 0
            best = go(i + 1, holding)
            if holding:
                best = max(best, prices[i] + go(i + 2, False))
            else:
                best = max(best, -prices[i] + go(i + 1, True))
            return best

        return go(0, False)
'''),

    P(114, "Coin Change II", "Medium", "change",
      r'''
`coins` lists coin denominations (each in unlimited supply) and `amount` is a target sum.

Return the number of different combinations of coins that add up to exactly `amount`. Orders do not matter (`1 + 2` and `2 + 1` are the same combination). If no combination works, return `0`. An amount of `0` has exactly one combination: using no coins.

## Examples

```
Input:  amount = 4, coins = [1, 2, 3]
Output: 4          # 1+1+1+1, 1+1+2, 2+2, 1+3

Input:  amount = 3, coins = [2]
Output: 0
```

## Constraints

- `1 <= len(coins) <= 100`
- `1 <= coins[i] <= 1000`, all distinct
- `0 <= amount <= 1000`

## Hints

- Process one coin at a time and update `ways[a] += ways[a - coin]`, going upwards. Looping over coins on the outside avoids counting orderings twice.
''',
      r'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def change(self, amount, coins):
        ways = [1] + [0] * amount
        for c in coins:
            for a in range(c, amount + 1):
                ways[a] += ways[a - c]
        return ways[amount]
''',
      [([4, [1, 2, 3]], 4), ([5, [1, 2, 5]], 4), ([3, [2]], 0), ([10, [10]], 1), ([0, [7]], 1), ([7, [2, 3]], 1)],
      gen=lambda rng: [[rng.randint(0, 20), rng.sample(range(1, 10), rng.randint(1, 4))] for _ in range(5)]
      + [[1000, [1, 2, 5, 10, 20, 50]], [800, [3, 7, 11, 13, 29, 41, 53]], [500, [1] + list(range(2, 100, 7))]],
      small=lambda rng: [rng.randint(0, 12), rng.sample(range(1, 8), rng.randint(1, 3))],
      brute=r'''
class Solution:
    def change(self, amount, coins):
        def go(i, left):
            if left == 0:
                return 1
            if i == len(coins) or left < 0:
                return 0
            return go(i, left - coins[i]) + go(i + 1, left)

        return go(0, amount)
'''),

    P(115, "Target Sum", "Medium", "findTargetSumWays",
      r'''
You are given a list of non-negative integers `nums` and an integer `target`. Put a `+` or a `-` in front of every number, then add them up.

Return the number of different sign assignments whose total equals `target`.

## Examples

```
Input:  nums = [2, 2, 2], target = 2
Output: 3          # +2+2-2, +2-2+2, -2+2+2

Input:  nums = [1, 1, 1, 1, 1], target = 3
Output: 5
```

## Constraints

- `1 <= len(nums) <= 20`
- `0 <= nums[i] <= 1000`, and `sum(nums) <= 1000`
- `-1000 <= target <= 1000`

## Hints

- Track how many ways each running total can be reached. The totals form a small dictionary.
- Or turn it into "how many subsets sum to `(total + target) / 2`".
''',
      r'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass
''',
      r'''
from collections import Counter


class Solution:
    def findTargetSumWays(self, nums, target):
        ways = Counter({0: 1})
        for x in nums:
            nxt = Counter()
            for total, count in ways.items():
                nxt[total + x] += count
                nxt[total - x] += count
            ways = nxt
        return ways[target]
''',
      [([[2, 2, 2], 2], 3), ([[1, 1, 1, 1, 1], 3], 5), ([[1], 1], 1), ([[1], 2], 0), ([[1, 0], 1], 2),
       ([[0, 0, 0], 0], 8), ([[1, 2, 3], 0], 2), ([[5, 5], 0], 2)],
      gen=lambda rng: [[_ints(rng, n, 0, 9), rng.randint(-10, 10)] for n in (3, 6, 10, 14)]
      + [[_ints(rng, 20, 0, 40), 0], [[1] * 20, 4], [[0] * 15 + [1], 1]],
      small=lambda rng: [_ints(rng, rng.randint(1, 9), 0, 6), rng.randint(-8, 8)],
      brute=r'''
from itertools import product


class Solution:
    def findTargetSumWays(self, nums, target):
        return sum(sum(s * x for s, x in zip(signs, nums)) == target for signs in product((1, -1), repeat=len(nums)))
'''),

    P(116, "Interleaving String", "Medium", "isInterleave",
      r'''
Given strings `s1`, `s2` and `s3`, return `True` if `s3` can be formed by interleaving `s1` and `s2`: split each of them into pieces, then alternate pieces from `s1` and `s2` while keeping the order of letters inside each string.

Put simply, you read through `s3` and, at each letter, take it from the front of what remains of `s1` or of `s2`.

## Examples

```
Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: True

Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: False
```

## Constraints

- `0 <= len(s1), len(s2) <= 100`, and `0 <= len(s3) <= 200`
- All strings consist of lowercase English letters.

## Hints

- `dp[i][j]` says whether the first `i` letters of `s1` and the first `j` of `s2` can form the first `i + j` letters of `s3`.
''',
      r'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass
''',
      r'''
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                    continue
                ok = False
                if i and dp[j] and s1[i - 1] == s3[i + j - 1]:
                    ok = True
                if j and dp[j - 1] and s2[j - 1] == s3[i + j - 1]:
                    ok = True
                dp[j] = ok
        return dp[len(s2)]
''',
      [(["aabcc", "dbbca", "aadbbcbcac"], True), (["aabcc", "dbbca", "aadbbbaccc"], False), (["", "", ""], True),
       (["a", "", "a"], True), (["", "", "a"], False), (["a", "b", "ab"], True), (["a", "b", "ba"], True),
       (["ab", "cd", "acbd"], True), (["ab", "cd", "abdc"], False), (["aa", "ab", "aaba"], True)],
      gen=_interleave_gen,
      small=lambda rng: _interleave(rng, _word(rng, rng.randint(0, 4), "ab"), _word(rng, rng.randint(0, 4), "ab"), rng.random() < 0.5),
      brute=r'''
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s3:
            return True
        if s1 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]):
            return True
        return bool(s2) and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:])
'''),

    P(117, "Longest Increasing Path in a Matrix", "Hard", "longestIncreasingPath",
      r'''
`matrix` is a grid of integers. From any cell you may move up, down, left or right (not diagonally, and not outside the grid).

Return the length of the longest path in which every step goes to a strictly larger value.

## Examples

```
Input:  matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
Output: 4          # 1 -> 2 -> 6 -> 9

Input:  matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
Output: 4          # 3 -> 4 -> 5 -> 6
```

## Constraints

- `1 <= rows, cols <= 50`
- `0 <= matrix[i][j] <= 10^4`

## Hints

- The longest path starting at a cell never depends on how you got there, so cache it (memoised DFS).
''',
      r'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        pass
''',
      r'''
class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def go(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            best = 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + go(nr, nc))
            memo[(r, c)] = best
            return best

        return max(go(r, c) for r in range(rows) for c in range(cols))
''',
      [([[[9, 9, 4], [6, 6, 8], [2, 1, 1]]], 4), ([[[3, 4, 5], [3, 2, 6], [2, 2, 1]]], 4), ([[[1]]], 1), ([[[1, 2]]], 2),
       ([[[1, 1]]], 1), ([[[5, 4], [6, 3]]], 4)],
      gen=_path_gen,
      small=lambda rng: [_matrix(rng, rng.randint(1, 3), rng.randint(1, 3), 6)],
      brute=r'''
class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        def go(r, c):
            best = 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + go(nr, nc))
            return best

        return max(go(r, c) for r in range(rows) for c in range(cols))
'''),

    P(118, "Distinct Subsequences", "Hard", "numDistinct",
      r'''
Given strings `s` and `t`, return the number of distinct subsequences of `s` that are equal to `t`. Subsequences made from different positions of `s` count separately, even if the text is the same.

## Examples

```
Input:  s = "caat", t = "cat"
Output: 2          # use either 'a'

Input:  s = "babgbag", t = "bag"
Output: 5
```

## Constraints

- `1 <= len(s) <= 1000`, `1 <= len(t) <= 1000`
- Both strings consist of English letters.
- The tests are chosen so the answer fits in a 32-bit integer.

## Hints

- `dp[i][j]` is the number of ways the first `j` letters of `t` appear in the first `i` letters of `s`. If `s[i-1] == t[j-1]` you may use that letter or skip it.
''',
      r'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass
''',
      r'''
class Solution:
    def numDistinct(self, s, t):
        dp = [1] + [0] * len(t)
        for ch in s:
            for j in range(len(t), 0, -1):
                if t[j - 1] == ch:
                    dp[j] += dp[j - 1]
        return dp[len(t)]
''',
      [(["caat", "cat"], 2), (["rabbbit", "rabbit"], 3), (["babgbag", "bag"], 5), (["a", "a"], 1), (["a", "b"], 0),
       (["aaa", "aa"], 3), (["abc", "abc"], 1), (["aaaa", "aa"], 6)],
      gen=lambda rng: [[_word(rng, rng.randint(1, 10), "ab"), _word(rng, rng.randint(1, 4), "ab")] for _ in range(5)]
      + [["a" * 30, "a" * 15], [_word(rng, 1000, "abcdefghijklmnopqrstuvwxyz"), _word(rng, 4, "abcdefghijklmnopqrstuvwxyz")],
         [_word(rng, 1000, "ab"), "ab" * 2], ["ab" * 15, "ab" * 6]],
      small=lambda rng: [_word(rng, rng.randint(1, 9), "ab"), _word(rng, rng.randint(1, 4), "ab")],
      brute=r'''
class Solution:
    def numDistinct(self, s, t):
        if not t:
            return 1
        if not s:
            return 0
        total = self.numDistinct(s[1:], t)
        if s[0] == t[0]:
            total += self.numDistinct(s[1:], t[1:])
        return total
'''),

    P(119, "Edit Distance", "Medium", "minDistance",
      r'''
Return the minimum number of single-character operations needed to turn `word1` into `word2`. The allowed operations are:

- insert a character,
- delete a character,
- replace a character with another.

## Examples

```
Input:  word1 = "monkeys", word2 = "money"
Output: 2

Input:  word1 = "horse", word2 = "ros"
Output: 3
```

## Constraints

- `0 <= len(word1), len(word2) <= 500`
- Both words consist of lowercase English letters.

## Hints

- `dp[i][j]` is the distance between the first `i` letters of `word1` and the first `j` of `word2`. If the last letters match it equals `dp[i-1][j-1]`; otherwise 1 plus the best of insert, delete, replace.
''',
      r'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass
''',
      r'''
class Solution:
    def minDistance(self, word1, word2):
        prev = list(range(len(word2) + 1))
        for i, a in enumerate(word1, 1):
            cur = [i]
            for j, b in enumerate(word2, 1):
                cur.append(prev[j - 1] if a == b else 1 + min(prev[j - 1], prev[j], cur[j - 1]))
            prev = cur
        return prev[-1]
''',
      [(["monkeys", "money"], 2), (["horse", "ros"], 3), (["intention", "execution"], 5), (["", "a"], 1), (["a", ""], 1),
       (["", ""], 0), (["abc", "abc"], 0), (["sea", "eat"], 2), (["kitten", "sitting"], 3)],
      gen=lambda rng: [[_word(rng, rng.randint(0, 8), "abc"), _word(rng, rng.randint(0, 8), "abc")] for _ in range(5)]
      + [[_word(rng, 500, "abcd"), _word(rng, 480, "abcd")], [_word(rng, 500, "ab"), _word(rng, 500, "ba")]],
      small=lambda rng: [_word(rng, rng.randint(0, 5), "abc"), _word(rng, rng.randint(0, 5), "abc")],
      brute=r'''
from functools import lru_cache


class Solution:
    def minDistance(self, word1, word2):
        @lru_cache(None)
        def go(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return go(i + 1, j + 1)
            return 1 + min(go(i + 1, j), go(i, j + 1), go(i + 1, j + 1))

        return go(0, 0)
'''),

    P(120, "Burst Balloons", "Hard", "maxCoins",
      r'''
There are `n` balloons, and balloon `i` has the number `nums[i]` painted on it. You burst every balloon, one at a time. When you burst balloon `i` you earn `left * nums[i] * right` coins, where `left` and `right` are the numbers on the balloons currently next to it. If a neighbour does not exist, treat it as a balloon with the number `1`.

Return the maximum number of coins you can collect by choosing the best order.

## Examples

```
Input:  nums = [3, 1, 5, 8]
Output: 167        # burst 1, 5, 3, 8

Input:  nums = [1, 5]
Output: 10
```

## Constraints

- `1 <= len(nums) <= 60`
- `0 <= nums[i] <= 100`

## Hints

- Think of the last balloon to burst inside a range. Its neighbours are then fixed (the range's borders), which splits the problem into two independent smaller ranges.
''',
      r'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def maxCoins(self, nums):
        a = [1] + nums + [1]
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for lo in range(n - length):
                hi = lo + length
                dp[lo][hi] = max(dp[lo][k] + dp[k][hi] + a[lo] * a[k] * a[hi] for k in range(lo + 1, hi))
        return dp[0][n - 1]
''',
      [([[4, 2, 3, 7]], 143), ([[3, 1, 5, 8]], 167), ([[1, 5]], 10), ([[1]], 1), ([[5]], 5), ([[2, 3]], 9)],
      gen=lambda rng: [[_ints(rng, n, 0, 9)] for n in (3, 5, 8, 12)] + [[_ints(rng, 60, 0, 100)], [[100] * 60]],
      small=lambda rng: [_ints(rng, rng.randint(1, 7), 0, 9)],
      brute=r'''
from itertools import permutations


class Solution:
    def maxCoins(self, nums):
        best = 0
        for order in permutations(range(len(nums))):
            alive = list(range(len(nums)))
            total = 0
            for i in order:
                p = alive.index(i)
                left = nums[alive[p - 1]] if p else 1
                right = nums[alive[p + 1]] if p + 1 < len(alive) else 1
                total += left * nums[i] * right
                alive.pop(p)
            best = max(best, total)
        return best
'''),

    P(121, "Regular Expression Matching", "Hard", "isMatch",
      r'''
Implement matching of the string `s` against the pattern `p`, where the pattern supports two special characters:

- `.` matches any single character.
- `*` matches zero or more copies of the character just before it.

The pattern must match the entire string `s`, not just part of it. Return `True` if it does, otherwise `False`.

## Examples

```
Input:  s = "aa", p = "a*"
Output: True

Input:  s = "ab", p = ".*"
Output: True

Input:  s = "mississippi", p = "mis*is*p*."
Output: False
```

## Constraints

- `0 <= len(s) <= 30`, `0 <= len(p) <= 30`
- `s` contains only lowercase letters. `p` contains lowercase letters, `.` and `*`.
- Every `*` follows a letter or a `.`, so patterns like `*a` or `a**` do not occur.

## Hints

- Let `dp[i][j]` mean "first `i` letters of `s` match first `j` of `p`". A `*` either matches zero copies (skip two pattern characters) or consumes one more letter.
''',
      r'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass
''',
      r'''
class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or (p[j - 2] in (s[i - 1], ".") and dp[i - 1][j])
                else:
                    dp[i][j] = p[j - 1] in (s[i - 1], ".") and dp[i - 1][j - 1]
        return dp[m][n]
''',
      [(["aa", "a"], False), (["aa", "a*"], True), (["ab", ".*"], True), (["aab", "c*a*b"], True),
       (["mississippi", "mis*is*p*."], False), (["", "a*"], True), (["a", ""], False), (["", ""], True),
       (["aaa", "a*a"], True), (["ab", ".*c"], False), (["aaa", "ab*a*c*a"], True), (["a", "ab*"], True)],
      gen=_regex_gen,
      small=lambda rng: [_word(rng, rng.randint(0, 6), "ab"), _regex(rng, rng.randint(0, 4))],
      brute=r'''
import re


class Solution:
    def isMatch(self, s, p):
        return re.fullmatch(p, s) is not None
'''),
]
