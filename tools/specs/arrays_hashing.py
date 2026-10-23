from spec import P

CATEGORY = "arrays-hashing"


def _grid(rng):
    digits = list(range(1, 10))
    rng.shuffle(digits)
    return [[str(digits[(r * 3 + r // 3 + c) % 9]) for c in range(9)] for r in range(9)]


def _blank(rng, grid, p):
    return [[v if rng.random() < p else "." for v in row] for row in grid]


def _sudoku_cases(rng):
    out = []
    for _ in range(4):
        out.append([_blank(rng, _grid(rng), rng.choice([0.2, 0.5, 1.0]))])
    for _ in range(4):
        g = _blank(rng, _grid(rng), 0.6)
        r, c = rng.randrange(9), rng.randrange(9)
        r2, c2 = rng.randrange(9), rng.randrange(9)
        if g[r2][c2] != ".":
            g[r][c] = g[r2][c2]
        out.append([g])
    for _ in range(4):
        out.append([[[rng.choice(".....123456789") for _ in range(9)] for _ in range(9)]])
    return out


def _sudoku_small(rng):
    return _sudoku_cases(rng)[rng.randrange(12)]


PROBLEMS = [
    P(6, "Encode and Decode Strings", "Medium", "encode",
      r'''
Design an algorithm that turns a list of strings into one single string (`encode`), and turns that string back into the original list (`decode`).

The two methods are called on separate `Solution` objects, so nothing may be remembered between them: everything needed to rebuild the list must be inside the encoded string. Strings can contain any characters, including digits, `#`, and separators you might be tempted to use. Do not use built-in serialization helpers.

## Examples

```
Input:  ["neet", "code", "love", "you"]
decode(encode(...)) must return ["neet", "code", "love", "you"]

Input:  ["we", "say", ":", "yes"]
decode(encode(...)) must return ["we", "say", ":", "yes"]
```

## Constraints

- `0 <= len(strs) <= 100`
- `0 <= len(strs[i]) <= 200`
- Strings may contain any ASCII character, and may be empty.

## Hints

- A separator character is not safe, because a string might contain it.
- What if each string is stored together with its own length?
''',
      r'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass
''',
      r'''
class Solution:
    def encode(self, strs):
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        out, i = [], 0
        while i < len(s):
            j = s.index("#", i)
            n = int(s[i:j])
            out.append(s[j + 1:j + 1 + n])
            i = j + 1 + n
        return out
''',
      [([x], x) for x in [
          ["neet", "code", "love", "you"], ["we", "say", ":", "yes"], [], [""], ["", ""],
          ["#"], ["4#abc", "3#", "#3"], ["a#b", "12", "0#"], ["1", "2", "3"],
          ["héllo", "wörld"], ["", "x", ""], ["#" * 50, "9" * 50],
      ]],
      roundtrip={"type": "plain", "class": "Solution", "encode": "encode", "decode": "decode"},
      gen=lambda rng: [[[
          "".join(rng.choice("#0123456789ab:;| ") for _ in range(rng.randint(0, 40)))
          for _ in range(n)]] for n in (5, 40, 100, 100)],
      ),

    P(7, "Product of Array Except Self", "Medium", "productExceptSelf",
      r'''
Given an integer list `nums`, return a list `output` where `output[i]` is the product of every element of `nums` except `nums[i]`.

Solve it in O(n) time without using division.

## Examples

```
Input:  nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]

Input:  nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]
```

## Constraints

- `2 <= len(nums) <= 10000`
- `-20 <= nums[i] <= 20` for the small cases; products of any prefix or suffix fit in a 32-bit integer.

## Hints

- Think of "everything to the left of i" multiplied by "everything to the right of i".
- You can build both with two passes over the list.
''',
      r'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass
''',
      r'''
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        out = [1] * n
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]
        return out
''',
      [([[1, 2, 4, 6]], [48, 24, 12, 8]), ([[-1, 0, 1, 2, 3]], [0, -6, 0, 0, 0]),
       ([[2, 3]], [3, 2]), ([[0, 0]], [0, 0]), ([[1, 1, 1]], [1, 1, 1]),
       ([[5, 0, 2]], [0, 10, 0]), ([[-2, -3, 4]], [-12, -8, 6]),
       ([[0, 4, 5]], [20, 0, 0]), ([[3, -3]], [-3, 3])],
      gen=lambda rng: [[[rng.randint(-5, 5) for _ in range(rng.randint(2, 12))]] for _ in range(3)]
      + [[[rng.choice([-1, 0, 1]) for _ in range(10000)]]]
      + [[[rng.choice([-1, 1]) for _ in range(10000)]]],
      small=lambda rng: [[rng.randint(-4, 4) for _ in range(rng.randint(2, 7))]],
      brute=r'''
class Solution:
    def productExceptSelf(self, nums):
        out = []
        for i in range(len(nums)):
            p = 1
            for j, v in enumerate(nums):
                if j != i:
                    p *= v
            out.append(p)
        return out
'''),

    P(8, "Valid Sudoku", "Medium", "isValidSudoku",
      r'''
You are given a 9 x 9 Sudoku board as a list of lists of single-character strings. Empty cells are `"."`.

Return `True` if the filled cells do not break any Sudoku rule, otherwise `False`. A board is valid when:

- each row has no repeated digit,
- each column has no repeated digit,
- each of the nine 3 x 3 boxes has no repeated digit.

You only check the filled cells. The board does not have to be solvable.

## Examples

```
A board with 5 at (0,0) and another 5 later in the same row  ->  False
A board with only 5 at (0,0) and 3 at (0,1)                  ->  True
```

## Constraints

- `len(board) == 9` and `len(board[i]) == 9`
- Each cell is `"1"` to `"9"` or `"."`.

## Hints

- Keep one set per row, per column, and per box.
- The box for cell `(r, c)` is `(r // 3, c // 3)`.
''',
      r'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pass
''',
      r'''
class Solution:
    def isValidSudoku(self, board):
        seen = set()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                keys = [("r", r, v), ("c", c, v), ("b", r // 3, c // 3, v)]
                if any(k in seen for k in keys):
                    return False
                seen.update(keys)
        return True
''',
      [
          ([[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]], True),
          ([[["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]], False),
          ([[["."] * 9 for _ in range(9)]], True),
          ([[["1", ".", ".", ".", ".", ".", ".", ".", "1"]] + [["."] * 9 for _ in range(8)]], False),
          ([[["2"] + ["."] * 8] + [["."] * 9 for _ in range(7)] + [["2"] + ["."] * 8]], False),
          ([[["1"] + ["."] * 8, [".", "1"] + ["."] * 7] + [["."] * 9 for _ in range(7)]], False),
          ([[["1"] + ["."] * 8, ["."] * 3 + ["1"] + ["."] * 5] + [["."] * 9 for _ in range(7)]], True),
      ],
      gen=_sudoku_cases, small=_sudoku_small,
      brute=r'''
class Solution:
    def isValidSudoku(self, board):
        cells = [(r, c) for r in range(9) for c in range(9) if board[r][c] != "."]
        for i, (r1, c1) in enumerate(cells):
            for r2, c2 in cells[i + 1:]:
                if board[r1][c1] == board[r2][c2] and (
                    r1 == r2 or c1 == c2 or (r1 // 3, c1 // 3) == (r2 // 3, c2 // 3)
                ):
                    return False
        return True
'''),

    P(9, "Longest Consecutive Sequence", "Medium", "longestConsecutive",
      r'''
Given an unsorted list of integers `nums`, return the length of the longest run of consecutive integers that all appear in the list (for example 4, 5, 6, 7). The numbers do not need to be next to each other in the list.

Your solution must run in O(n) time.

## Examples

```
Input:  nums = [2, 20, 4, 10, 3, 4, 5]
Output: 4          # 2, 3, 4, 5

Input:  nums = [0, 3, 2, 5, 4, 6, 1, 1]
Output: 7          # 0 through 6
```

## Constraints

- `0 <= len(nums) <= 100000`
- `-10^9 <= nums[i] <= 10^9`

## Hints

- Sorting works but is O(n log n).
- Put everything in a set. Only start counting from numbers that have no predecessor (`x - 1` not in the set).
''',
      r'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                y = x
                while y + 1 in s:
                    y += 1
                best = max(best, y - x + 1)
        return best
''',
      [([[2, 20, 4, 10, 3, 4, 5]], 4), ([[0, 3, 2, 5, 4, 6, 1, 1]], 7), ([[]], 0), ([[1]], 1),
       ([[5, 5, 5]], 1), ([[-1, -2, 0, 10]], 3), ([[100, 4, 200, 1, 3, 2]], 4),
       ([[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]], 7), ([[1000000000, -1000000000]], 1)],
      gen=lambda rng: [[rng.sample(range(-10, 10), rng.randint(0, 12))] for _ in range(3)]
      + [[rng.sample(range(10000), 10000)]]
      + [[rng.sample(range(0, 1000000), 10000)]]
      + [[[x for x in rng.sample(range(12000), 12000) if x % 10 != 0]]],
      small=lambda rng: [[rng.randint(-8, 8) for _ in range(rng.randint(0, 10))]],
      brute=r'''
class Solution:
    def longestConsecutive(self, nums):
        ordered = sorted(set(nums))
        best = cur = 0
        for i, x in enumerate(ordered):
            cur = cur + 1 if i and x == ordered[i - 1] + 1 else 1
            best = max(best, cur)
        return best
'''),
]
