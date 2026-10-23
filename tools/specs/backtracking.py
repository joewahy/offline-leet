from spec import P

CATEGORY = "backtracking"


def _distinct(rng, n, lo=-9, hi=9):
    return rng.sample(range(lo, hi + 1), n)


def _combo(rng, k, target, hi=9):
    return [rng.sample(range(2, hi + 1), k), target]


def _combo2(rng, n, target):
    return [[rng.randint(1, 8) for _ in range(n)], target]


def _board(rng, rows, cols, letters):
    return [[rng.choice(letters) for _ in range(cols)] for _ in range(rows)]


def _word(rng, n, letters):
    return "".join(rng.choice(letters) for _ in range(n))


def _words2(rng):
    board = _board(rng, 10, 10, "abcde")
    words = list({_word(rng, rng.randint(4, 8), "abcde") for _ in range(2500)})
    # make sure some words really are on the board
    for _ in range(40):
        r, c = rng.randrange(10), rng.randrange(10)
        path, seen = [board[r][c]], {(r, c)}
        for _ in range(rng.randint(2, 7)):
            options = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                       if 0 <= r + dr < 10 and 0 <= c + dc < 10 and (r + dr, c + dc) not in seen]
            if not options:
                break
            r, c = rng.choice(options)
            seen.add((r, c))
            path.append(board[r][c])
        words.append("".join(path))
    return [board, sorted(set(words))]


PROBLEMS = [
    P(68, "Subsets", "Medium", "subsets",
      r'''
Given a list `nums` of distinct integers, return every possible subset (the power set), including the empty subset and `nums` itself. The subsets, and the numbers inside each subset, may be in any order. No subset may appear twice.

## Examples

```
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Input:  nums = [7]
Output: [[], [7]]
```

## Constraints

- `1 <= len(nums) <= 10`
- `-10 <= nums[i] <= 10`
- All values are distinct.

## Hints

- For each number you have two choices: include it or skip it.
''',
      r'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def subsets(self, nums):
        out = [[]]
        for x in nums:
            out += [s + [x] for s in out]
        return out
''',
      [([[1, 2, 3]], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]), ([[7]], [[], [7]]),
       ([[0]], [[], [0]]), ([[1, 2]], [[], [1], [2], [1, 2]]), ([[-1, 1]], [[], [-1], [1], [-1, 1]])],
      compare="unordered_nested",
      gen=lambda rng: [[_distinct(rng, n)] for n in (3, 5, 8, 10)],
      small=lambda rng: [_distinct(rng, rng.randint(1, 6))],
      brute=r'''
from itertools import combinations


class Solution:
    def subsets(self, nums):
        return [list(c) for r in range(len(nums) + 1) for c in combinations(nums, r)]
'''),

    P(69, "Combination Sum", "Medium", "combinationSum",
      r'''
`nums` holds distinct positive integers and `target` is a positive integer. Return every unique combination of numbers from `nums` that adds up to `target`. The same number may be used any number of times. Two combinations are different if they use some number a different number of times.

The combinations, and the numbers inside each one, may be returned in any order.

## Examples

```
Input:  nums = [2, 5, 6, 9], target = 9
Output: [[2, 2, 5], [9]]

Input:  nums = [3, 4, 5], target = 16
Output: [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]
```

## Constraints

- `1 <= len(nums) <= 20`
- `2 <= nums[i] <= 30`, all distinct
- `2 <= target <= 40`
- The number of combinations is at most 150.

## Hints

- Pick a number, subtract it from the target, and recurse. Move forward in the list so you do not produce the same combination in a different order.
''',
      r'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def combinationSum(self, nums, target):
        out = []

        def go(start, remaining, path):
            if remaining == 0:
                out.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] <= remaining:
                    path.append(nums[i])
                    go(i, remaining - nums[i], path)
                    path.pop()

        go(0, target, [])
        return out
''',
      [([[2, 5, 6, 9], 9], [[2, 2, 5], [9]]), ([[3, 4, 5], 16], [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]),
       ([[3], 5], []), ([[2], 2], [[2]]), ([[2, 3, 6, 7], 7], [[2, 2, 3], [7]]), ([[2, 3, 5], 8], [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
       ([[2, 4], 7], [])],
      compare="unordered_nested",
      gen=lambda rng: [_combo(rng, rng.randint(1, 4), rng.randint(2, 20)) for _ in range(4)]
      + [[[2, 3, 5, 7], 30], [[2, 3, 5], 40]],
      small=lambda rng: _combo(rng, rng.randint(1, 4), rng.randint(2, 16), 8),
      brute=r'''
from itertools import product


class Solution:
    def combinationSum(self, nums, target):
        out = []
        for counts in product(*[range(target // n + 1) for n in nums]):
            if sum(c * n for c, n in zip(counts, nums)) == target:
                out.append([n for c, n in zip(counts, nums) for _ in range(c)])
        return out
'''),

    P(70, "Permutations", "Medium", "permute",
      r'''
Given a list `nums` of distinct integers, return all possible orderings (permutations) of its elements. The permutations may be returned in any order.

## Examples

```
Input:  nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Input:  nums = [1]
Output: [[1]]
```

## Constraints

- `1 <= len(nums) <= 6`
- `-10 <= nums[i] <= 10`, all distinct

## Hints

- Choose any unused number for the first position, then recurse on the rest.
''',
      r'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def permute(self, nums):
        out = []

        def go(path, rest):
            if not rest:
                out.append(path)
                return
            for i in range(len(rest)):
                go(path + [rest[i]], rest[:i] + rest[i + 1:])

        go([], nums)
        return out
''',
      [([[1, 2, 3]], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]), ([[1]], [[1]]),
       ([[0, 1]], [[0, 1], [1, 0]]), ([[5, -5]], [[5, -5], [-5, 5]])],
      compare="unordered_outer",
      gen=lambda rng: [[_distinct(rng, n, -10, 10)] for n in (3, 4, 5, 6)],
      small=lambda rng: [_distinct(rng, rng.randint(1, 5), -10, 10)],
      brute=r'''
from itertools import permutations


class Solution:
    def permute(self, nums):
        return [list(p) for p in permutations(nums)]
'''),

    P(71, "Subsets II", "Medium", "subsetsWithDup",
      r'''
`nums` may contain duplicate integers. Return every possible subset, but with no duplicate subsets (two subsets are the same if they contain the same values the same number of times). The subsets, and the numbers inside them, may be in any order.

## Examples

```
Input:  nums = [1, 2, 1]
Output: [[], [1], [1, 2], [1, 1], [1, 1, 2], [2]]

Input:  nums = [7, 7]
Output: [[], [7], [7, 7]]
```

## Constraints

- `1 <= len(nums) <= 10`
- `-10 <= nums[i] <= 10`

## Hints

- Sort first. When you skip a value at some position, skip all of its equal neighbours too.
''',
      r'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        out = []

        def go(start, path):
            out.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                go(i + 1, path)
                path.pop()

        go(0, [])
        return out
''',
      [([[1, 2, 1]], [[], [1], [1, 2], [1, 1], [1, 1, 2], [2]]), ([[7, 7]], [[], [7], [7, 7]]), ([[0]], [[], [0]]),
       ([[1, 1, 1]], [[], [1], [1, 1], [1, 1, 1]]), ([[2, 2]], [[], [2], [2, 2]]),
       ([[1, 2, 2]], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])],
      compare="unordered_nested",
      gen=lambda rng: [[[rng.randint(-3, 3) for _ in range(n)]] for n in (3, 5, 7, 9, 10)],
      small=lambda rng: [[rng.randint(-2, 2) for _ in range(rng.randint(1, 7))]],
      brute=r'''
from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums):
        found = {tuple(sorted(c)) for r in range(len(nums) + 1) for c in combinations(nums, r)}
        return [list(t) for t in found]
'''),

    P(72, "Combination Sum II", "Medium", "combinationSum2",
      r'''
`candidates` is a list of positive integers that may contain duplicates, and `target` is a positive integer. Return every unique combination of candidates that adds up to `target`. Each candidate may be used at most once, and the result must not contain duplicate combinations.

The combinations, and the numbers inside them, may be returned in any order.

## Examples

```
Input:  candidates = [9, 2, 5, 2, 1], target = 9
Output: [[9], [2, 2, 5]]

Input:  candidates = [2, 5, 2, 1, 2], target = 5
Output: [[1, 2, 2], [5]]
```

## Constraints

- `1 <= len(candidates) <= 30`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Hints

- Sort the list. At each depth, skip a value that equals the previous one you already tried at that depth.
''',
      r'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def combinationSum2(self, candidates, target):
        nums = sorted(candidates)
        out = []

        def go(start, remaining, path):
            if remaining == 0:
                out.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                go(i + 1, remaining - nums[i], path)
                path.pop()

        go(0, target, [])
        return out
''',
      [([[9, 2, 5, 2, 1], 9], [[9], [2, 2, 5]]), ([[10, 1, 2, 7, 6, 1, 5], 8], [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
       ([[2, 5, 2, 1, 2], 5], [[1, 2, 2], [5]]), ([[2], 1], []), ([[1], 1], [[1]]), ([[1, 1, 1], 2], [[1, 1]]),
       ([[3, 1, 3, 5, 1, 1], 8], [[3, 5], [1, 1, 1, 5], [1, 1, 3, 3]])],
      compare="unordered_nested",
      gen=lambda rng: [_combo2(rng, rng.randint(3, 8), rng.randint(4, 14)) for _ in range(4)]
      + [[[1] * 12 + [2] * 8 + [3] * 6, 15], [[rng.randint(1, 8) for _ in range(22)], 25]],
      small=lambda rng: _combo2(rng, rng.randint(1, 8), rng.randint(1, 14)),
      brute=r'''
from itertools import combinations


class Solution:
    def combinationSum2(self, candidates, target):
        found = set()
        for r in range(len(candidates) + 1):
            for c in combinations(candidates, r):
                if sum(c) == target:
                    found.add(tuple(sorted(c)))
        return [list(t) for t in found]
'''),

    P(73, "Word Search", "Medium", "exist",
      r'''
Given a grid of characters `board` and a string `word`, return `True` if `word` can be spelled by walking through horizontally or vertically adjacent cells, starting anywhere. Each cell may be used at most once in a single path.

## Examples

```
Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: True

Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: False
```

## Constraints

- `1 <= rows, cols <= 6`
- `1 <= len(word) <= 15`
- `board` and `word` consist of English letters.

## Hints

- Start a depth-first search from each cell that matches the first letter. Mark cells as visited on the way in and unmark them on the way out.
''',
      r'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass
''',
      r'''
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
                return False
            keep, board[r][c] = board[r][c], "#"
            found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            board[r][c] = keep
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
''',
      [([[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"], True),
       ([[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"], True),
       ([[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"], False),
       ([[["a"]], "a"], True), ([[["a"]], "b"], False), ([[["a", "b"]], "ba"], True),
       ([[["a", "b"], ["c", "d"]], "abdca"], False), ([[["a", "b"], ["c", "d"]], "acdb"], True),
       ([[["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"], True)],
      gen=lambda rng: [[_board(rng, rng.randint(1, 4), rng.randint(1, 4), "ab"), _word(rng, rng.randint(1, 6), "ab")]
                       for _ in range(8)]
      + [[[["a"] * 4 for _ in range(4)], "a" * 10 + "b"], [[["a"] * 4 for _ in range(4)], "a" * 16],
         [[["a"] * 5 for _ in range(5)], "a" * 12 + "b"]],
      small=lambda rng: [_board(rng, rng.randint(1, 3), rng.randint(1, 3), "ab"), _word(rng, rng.randint(1, 5), "ab")],
      brute=r'''
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def go(r, c, i, used):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            used = used | {(r, c)}
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in used and go(nr, nc, i + 1, used):
                    return True
            return False

        return any(go(r, c, 0, frozenset()) for r in range(rows) for c in range(cols))
'''),

    P(74, "Palindrome Partitioning", "Medium", "partition",
      r'''
Split the string `s` into consecutive pieces so that every piece is a palindrome. Return every possible way to do this, as a list of lists of pieces. The ways may be returned in any order.

## Examples

```
Input:  s = "aab"
Output: [["a", "a", "b"], ["aa", "b"]]

Input:  s = "a"
Output: [["a"]]
```

## Constraints

- `1 <= len(s) <= 12`
- `s` consists of lowercase English letters.

## Hints

- Try every prefix that is a palindrome, then partition the remainder recursively.
''',
      r'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass
''',
      r'''
class Solution:
    def partition(self, s):
        out = []

        def go(start, path):
            if start == len(s):
                out.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1]:
                    path.append(piece)
                    go(end, path)
                    path.pop()

        go(0, [])
        return out
''',
      [(["aab"], [["a", "a", "b"], ["aa", "b"]]), (["a"], [["a"]]), (["aa"], [["a", "a"], ["aa"]]),
       (["aba"], [["a", "b", "a"], ["aba"]]), (["abc"], [["a", "b", "c"]]),
       (["aaa"], [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]])],
      compare="unordered_outer",
      gen=lambda rng: [[_word(rng, rng.randint(1, 8), "ab")] for _ in range(5)] + [["a" * 12], ["abababababab"]],
      small=lambda rng: [_word(rng, rng.randint(1, 8), "ab")],
      brute=r'''
class Solution:
    def partition(self, s):
        out = []
        n = len(s)
        for mask in range(1 << max(n - 1, 0)):
            pieces, last = [], 0
            for i in range(n - 1):
                if mask >> i & 1:
                    pieces.append(s[last:i + 1])
                    last = i + 1
            pieces.append(s[last:])
            if all(p == p[::-1] for p in pieces):
                out.append(pieces)
        return out
'''),

    P(75, "Letter Combinations of a Phone Number", "Medium", "letterCombinations",
      r'''
Each digit from `2` to `9` on a phone keypad maps to letters: `2 -> abc`, `3 -> def`, `4 -> ghi`, `5 -> jkl`, `6 -> mno`, `7 -> pqrs`, `8 -> tuv`, `9 -> wxyz`.

Given a string `digits`, return every letter combination it could spell, in any order. If `digits` is empty, return an empty list.

## Examples

```
Input:  digits = "34"
Output: ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]

Input:  digits = ""
Output: []
```

## Constraints

- `0 <= len(digits) <= 4`
- Each digit is between `'2'` and `'9'`.

## Hints

- Build one letter per digit, trying every letter that digit maps to.
''',
      r'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass
''',
      r'''
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        keys = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        out = [""]
        for d in digits:
            out = [prefix + c for prefix in out for c in keys[d]]
        return out
''',
      [(["34"], ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]), (["2"], ["a", "b", "c"]), ([""], []),
       (["9"], ["w", "x", "y", "z"]), (["23"], ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])],
      compare="unordered",
      gen=lambda rng: [["".join(rng.choice("23456789") for _ in range(n))] for n in (1, 2, 3, 4)] + [["7979"], ["9999"]],
      small=lambda rng: ["".join(rng.choice("23456789") for _ in range(rng.randint(0, 3)))],
      brute=r'''
from itertools import product


class Solution:
    def letterCombinations(self, digits):
        keys = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
        return ["".join(p) for p in product(*[keys[int(d) - 2] for d in digits])]
'''),

    P(76, "N-Queens", "Hard", "solveNQueens",
      r'''
Place `n` queens on an `n x n` chessboard so that no two queens attack each other (no two share a row, a column, or a diagonal).

Return every distinct solution. Each solution is a list of `n` strings, one per row, where `"Q"` is a queen and `"."` is an empty square. The solutions may be returned in any order.

## Examples

```
Input:  n = 4
Output: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]

Input:  n = 1
Output: [["Q"]]
```

## Constraints

- `1 <= n <= 8`

## Hints

- Place one queen per row. Track which columns and diagonals (`row - col` and `row + col`) are taken.
''',
      r'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass
''',
      r'''
class Solution:
    def solveNQueens(self, n):
        out = []
        cols, diag, anti = set(), set(), set()
        placed = []

        def go(r):
            if r == n:
                out.append(["." * c + "Q" + "." * (n - c - 1) for c in placed])
                return
            for c in range(n):
                if c in cols or r - c in diag or r + c in anti:
                    continue
                cols.add(c), diag.add(r - c), anti.add(r + c)
                placed.append(c)
                go(r + 1)
                placed.pop()
                cols.remove(c), diag.remove(r - c), anti.remove(r + c)

        go(0)
        return out
''',
      [([1], [["Q"]]), ([2], []), ([3], []),
       ([4], [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])],
      compare="unordered_outer",
      gen=lambda rng: [[5], [6], [7], [8]],
      small=lambda rng: [rng.randint(1, 6)],
      brute=r'''
from itertools import permutations


class Solution:
    def solveNQueens(self, n):
        out = []
        for perm in permutations(range(n)):
            if all(abs(perm[i] - perm[j]) != j - i for i in range(n) for j in range(i + 1, n)):
                out.append(["." * c + "Q" + "." * (n - c - 1) for c in perm])
        return out
'''),
]
