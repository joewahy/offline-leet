from spec import P

CATEGORY = "math-geometry"


def _square(rng, n, hi=99):
    return [[rng.randint(-hi, hi) for _ in range(n)] for _ in range(n)]


def _rect(rng, rows, cols, hi=99):
    return [[rng.randint(-hi, hi) for _ in range(cols)] for _ in range(rows)]


def _zeroes(rng, rows, cols, p):
    return [[0 if rng.random() < p else rng.randint(1, 9) for _ in range(cols)] for _ in range(rows)]


def _digits(rng, n):
    d = [rng.randint(0, 9) for _ in range(n)]
    d[0] = rng.randint(1, 9) if n > 1 else d[0]
    return d


def _number(rng, n):
    return str(rng.randint(10 ** (n - 1), 10 ** n - 1)) if n > 1 else str(rng.randint(0, 9))


def _pow_case(rng):
    n = rng.randint(-60, 60)
    return [round(rng.uniform(0.5, 1.5), 4), n]


HAPPY_SEEDS = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139]


def _happy_gen(rng):
    out = [[rng.choice(HAPPY_SEEDS)] for _ in range(4)] + [[rng.randint(2, 200)] for _ in range(6)]
    out += [[2147483647], [1000000000], [1111111], [999999999], [rng.randint(10 ** 8, 2 ** 31 - 1)]]
    return out


def _squares(rng, m, span):
    ops, params = ["DetectSquares"], [[]]
    for _ in range(m):
        if rng.random() < 0.5:
            ops.append("add")
        else:
            ops.append("count")
        params.append([[rng.randint(0, span), rng.randint(0, span)]])
    return [ops, params]


PROBLEMS = [
    P(136, "Rotate Image", "Medium", "rotate",
      r'''
`matrix` is an `n x n` grid of integers. Rotate it 90 degrees clockwise, in place: modify the given matrix directly and do not allocate another matrix. The function returns nothing.

## Examples

```
Input:  [[1, 2], [3, 4]]
Output: [[3, 1], [4, 2]]

Input:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Constraints

- `1 <= n <= 100`
- `-1000 <= matrix[i][j] <= 1000`

## Hints

- Transposing the matrix and then reversing each row gives a clockwise rotation.
- Or rotate four cells at a time, layer by layer.
''',
      r'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass
''',
      r'''
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
''',
      [([[[1, 2], [3, 4]]], [[3, 1], [4, 2]]), ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
       ([[[1]]], [[1]]),
       ([[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])],
      inplace=0,
      gen=lambda rng: [[_square(rng, n)] for n in (2, 3, 5, 8, 20)] + [[_square(rng, 100, 1000)]],
      small=lambda rng: [_square(rng, rng.randint(1, 6), 9)],
      brute=r'''
class Solution:
    def rotate(self, matrix):
        rotated = [list(row) for row in zip(*matrix[::-1])]
        for i, row in enumerate(rotated):
            matrix[i][:] = row
'''),

    P(137, "Spiral Matrix", "Medium", "spiralOrder",
      r'''
Given an `m x n` matrix, return all of its elements in spiral order: start at the top-left, go right along the top row, then down the right column, then left along the bottom row, then up the left column, and keep spiralling inwards.

## Examples

```
Input:  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input:  matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

## Constraints

- `1 <= m, n <= 100`
- `-100 <= matrix[i][j] <= 100`

## Hints

- Keep four boundaries (top, bottom, left, right) and shrink them after walking each side. Watch for a single remaining row or column.
''',
      r'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass
''',
      r'''
class Solution:
    def spiralOrder(self, matrix):
        out = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            out += matrix[top][left:right + 1]
            for r in range(top + 1, bottom + 1):
                out.append(matrix[r][right])
            if top < bottom:
                out += matrix[bottom][left:right][::-1]
            if left < right:
                for r in range(bottom - 1, top, -1):
                    out.append(matrix[r][left])
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return out
''',
      [([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
       ([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]), ([[[1]]], [1]),
       ([[[1, 2]]], [1, 2]), ([[[1], [2], [3]]], [1, 2, 3]), ([[[1, 2], [3, 4]]], [1, 2, 4, 3]),
       ([[[1, 2, 3], [4, 5, 6]]], [1, 2, 3, 6, 5, 4]), ([[[1, 2], [3, 4], [5, 6]]], [1, 2, 4, 6, 5, 3])],
      gen=lambda rng: [[_rect(rng, r, c)] for r, c in ((1, 7), (6, 1), (3, 5), (5, 3), (4, 4), (7, 6))] + [[_rect(rng, 100, 100)], [_rect(rng, 100, 37)]],
      small=lambda rng: [_rect(rng, rng.randint(1, 5), rng.randint(1, 5), 9)],
      brute=r'''
class Solution:
    def spiralOrder(self, matrix):
        grid = [list(r) for r in matrix]
        out = []
        while grid:
            out += grid.pop(0)
            grid = [list(r) for r in zip(*grid)][::-1]
        return out
'''),

    P(138, "Set Matrix Zeroes", "Medium", "setZeroes",
      r'''
`matrix` is an `m x n` grid of integers. If a cell is `0`, set its entire row and its entire column to `0`. Do it in place; the function returns nothing.

## Examples

```
Input:  [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

Input:  [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
```

## Constraints

- `1 <= m, n <= 100`
- `-1000 <= matrix[i][j] <= 1000`

## Hints

- Zeros you create must not cause more zeros. First record which rows and columns to clear, then clear them.
- You can store those markers in the first row and first column to use O(1) extra space.
''',
      r'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass
''',
      r'''
class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = {r for r in range(rows) for c in range(cols) if matrix[r][c] == 0}
        zero_cols = {c for r in range(rows) for c in range(cols) if matrix[r][c] == 0}
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
''',
      [([[[1, 1, 1], [1, 0, 1], [1, 1, 1]]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
       ([[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
       ([[[1]]], [[1]]), ([[[0]]], [[0]]), ([[[1, 0]]], [[0, 0]]), ([[[1, 2], [3, 4]]], [[1, 2], [3, 4]]),
       ([[[0, 1], [1, 1]]], [[0, 0], [0, 1]]), ([[[1, 1], [0, 1]]], [[0, 1], [0, 0]])],
      inplace=0,
      gen=lambda rng: [[_zeroes(rng, r, c, p)] for r, c, p in ((1, 4, 0.3), (4, 1, 0.3), (3, 3, 0.2), (5, 6, 0.1), (6, 5, 0.3))]
      + [[_zeroes(rng, 100, 100, 0.005)], [_zeroes(rng, 100, 100, 0.0)]],
      small=lambda rng: [_zeroes(rng, rng.randint(1, 5), rng.randint(1, 5), 0.25)],
      brute=r'''
class Solution:
    def setZeroes(self, matrix):
        original = [row[:] for row in matrix]
        for r, row in enumerate(original):
            for c, v in enumerate(row):
                if v == 0:
                    for k in range(len(matrix[0])):
                        matrix[r][k] = 0
                    for k in range(len(matrix)):
                        matrix[k][c] = 0
'''),

    P(139, "Happy Number", "Easy", "isHappy",
      r'''
Start with a positive integer `n`. Repeatedly replace it by the sum of the squares of its digits. If this process eventually reaches `1`, `n` is happy. If it falls into a loop that never reaches `1`, it is not.

Return `True` if `n` is a happy number, otherwise `False`.

## Examples

```
Input:  n = 100
Output: True       # 1^2 + 0^2 + 0^2 = 1

Input:  n = 101
Output: False
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Hints

- Remember the numbers you have already seen; seeing one twice means a cycle.
- Floyd's tortoise and hare also detects the cycle without extra memory.
''',
      r'''
class Solution:
    def isHappy(self, n: int) -> bool:
        pass
''',
      r'''
class Solution:
    def isHappy(self, n):
        def step(x):
            return sum(int(d) ** 2 for d in str(x))

        slow, fast = n, step(n)
        while fast != 1 and slow != fast:
            slow = step(slow)
            fast = step(step(fast))
        return fast == 1
''',
      [([100], True), ([101], False), ([1], True), ([2], False), ([19], True), ([7], True), ([4], False), ([10], True),
       ([28], True), ([1111111], True)],
      gen=_happy_gen,
      small=lambda rng: [rng.randint(1, 300)],
      brute=r'''
class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1
'''),

    P(140, "Plus One", "Easy", "plusOne",
      r'''
A non-negative integer is stored as a list of its decimal `digits`, most significant digit first, with no leading zeros (except the number `0` itself). Add one to the integer and return the resulting list of digits.

## Examples

```
Input:  digits = [1, 2, 3]
Output: [1, 2, 4]

Input:  digits = [9, 9]
Output: [1, 0, 0]
```

## Constraints

- `1 <= len(digits) <= 100`
- `0 <= digits[i] <= 9`

## Hints

- Work from the last digit. A `9` becomes `0` and carries; stop at the first digit that is not `9`.
''',
      r'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pass
''',
      r'''
class Solution:
    def plusOne(self, digits):
        digits = digits[:]
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
''',
      [([[1, 2, 3]], [1, 2, 4]), ([[9, 9]], [1, 0, 0]), ([[0]], [1]), ([[9]], [1, 0]), ([[1, 9, 9]], [2, 0, 0]),
       ([[4, 3, 2, 1]], [4, 3, 2, 2]), ([[8, 9, 9]], [9, 0, 0])],
      gen=lambda rng: [[_digits(rng, n)] for n in (2, 5, 12, 40)] + [[[9] * 100], [[9] * 99 + [8]], [[1] + [0] * 99]],
      small=lambda rng: [rng.choice([_digits(rng, rng.randint(1, 6)), [9] * rng.randint(1, 5)])],
      brute=r'''
class Solution:
    def plusOne(self, digits):
        return [int(c) for c in str(int("".join(map(str, digits))) + 1)]
'''),

    P(141, "Pow(x, n)", "Medium", "myPow",
      r'''
Implement `pow(x, n)`: return `x` raised to the power `n`. `x` is a floating-point number and `n` is an integer, which may be negative. Your answer is accepted if it is within `1e-5` of the exact value.

Do not use `**`, `pow`, or `math.pow`. Aim for O(log n) multiplications.

## Examples

```
Input:  x = 2.0, n = 10
Output: 1024.0

Input:  x = 2.0, n = -2
Output: 0.25
```

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `x` is not `0` when `n` is negative; the result is between `-10^4` and `10^4`.

## Hints

- Square the base and halve the exponent: `x^n = (x^2)^(n/2)`. Handle odd `n` with one extra multiplication, and negate `n` for the reciprocal.
''',
      r'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        pass
''',
      r'''
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result
''',
      [([2.0, 10], 1024.0), ([2.0, -2], 0.25), ([0.5, 2], 0.25), ([1.0, 100000], 1.0), ([2.0, 0], 1.0),
       ([-2.0, 3], -8.0), ([-2.0, 2], 4.0), ([0.0, 5], 0.0), ([2.0, -1], 0.5), ([2.0, 13], 8192.0)],
      compare="float",
      gen=lambda rng: [_pow_case(rng) for _ in range(6)]
      + [[1.0, 2147483647], [-1.0, 2147483647], [-1.0, -2147483648], [0.99999, 100000], [1.0000001, 1000000], [2.0, -10]],
      small=lambda rng: _pow_case(rng),
      brute=r'''
class Solution:
    def myPow(self, x, n):
        return x ** n
'''),

    P(142, "Multiply Strings", "Medium", "multiply",
      r'''
Two non-negative integers are given as decimal strings `num1` and `num2`. Return their product as a string.

You may not use a big-integer library or convert the input strings directly to integers; do the multiplication digit by digit, as on paper.

## Examples

```
Input:  num1 = "3", num2 = "4"
Output: "12"

Input:  num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints

- `1 <= len(num1), len(num2) <= 200`
- Digits only; no leading zeros except the number `0` itself.

## Hints

- The product has at most `len(num1) + len(num2)` digits. Digit `i` of one number times digit `j` of the other lands at position `i + j`.
''',
      r'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        pass
''',
      r'''
class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                total = res[i + j + 1] + (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                res[i + j + 1] = total % 10
                res[i + j] += total // 10
        start = 0
        while res[start] == 0:
            start += 1
        return "".join(map(str, res[start:]))
''',
      [(["3", "4"], "12"), (["111", "111"], "12321"), (["2", "3"], "6"), (["123", "456"], "56088"), (["0", "999"], "0"),
       (["999", "999"], "998001"), (["9133", "0"], "0"), (["1", "1"], "1"), (["12345678", "1"], "12345678")],
      gen=lambda rng: [[_number(rng, a), _number(rng, b)] for a, b in ((2, 2), (5, 3), (20, 20), (50, 7), (100, 100))]
      + [["9" * 200, "9" * 200], [_number(rng, 200), _number(rng, 200)], ["1" + "0" * 199, "1" + "0" * 199]],
      small=lambda rng: [_number(rng, rng.randint(1, 6)), _number(rng, rng.randint(1, 6))],
      brute=r'''
class Solution:
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))
'''),

    P(143, "Detect Squares", "Medium", "DetectSquares",
      r'''
Design a data structure that receives points on a 2D plane and counts axis-aligned squares.

Implement `DetectSquares`:

- `DetectSquares()` creates an empty structure.
- `add(point)` adds the point `[x, y]`. The same point may be added several times; each copy counts separately.
- `count(point)` returns the number of ways to choose three stored points that, together with the query `point`, form a square with positive area whose sides are parallel to the axes.

## Examples

```
add([3, 10]); add([11, 2]); add([3, 2])
count([11, 10])  -> 1
count([14, 8])   -> 0
add([11, 2])
count([11, 10])  -> 2
```

## Constraints

- `0 <= x, y <= 1000`
- At most `3000` calls are made.

## Hints

- Keep a count of each distinct point. For a query, try every stored point on the same diagonal and multiply the counts of the other two corners.
''',
      r'''
class DetectSquares:

    def __init__(self):
        pass

    def add(self, point: List[int]) -> None:
        pass

    def count(self, point: List[int]) -> int:
        pass
''',
      r'''
from collections import Counter


class DetectSquares:
    def __init__(self):
        self.counts = Counter()

    def add(self, point):
        self.counts[tuple(point)] += 1

    def count(self, point):
        x, y = point
        total = 0
        for (px, py), c in list(self.counts.items()):
            if abs(px - x) == abs(py - y) and px != x:
                total += c * self.counts[(px, y)] * self.counts[(x, py)]
        return total
''',
      [([["DetectSquares", "add", "add", "add", "count", "count", "add", "count"],
         [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]],
        [None, None, None, None, 1, 0, None, 2]),
       ([["DetectSquares", "count"], [[], [[1, 1]]]], [None, 0]),
       ([["DetectSquares", "add", "add", "add", "count"], [[], [[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]]]], [None, None, None, None, 1]),
       ([["DetectSquares", "add", "add", "add", "add", "count"], [[], [[1, 1]], [[1, 1]], [[2, 2]], [[2, 1]], [[1, 2]]]],
        [None, None, None, None, None, 2]),
       ([["DetectSquares", "add", "add", "add", "count"], [[], [[0, 0]], [[0, 2]], [[1, 1]], [[2, 0]]]], [None, None, None, None, 0])],
      design="DetectSquares",
      gen=lambda rng: [_squares(rng, 25, 2), _squares(rng, 60, 3), _squares(rng, 200, 4), _squares(rng, 3000, 20)],
      small=lambda rng: _squares(rng, rng.randint(1, 14), 2),
      brute=r'''
from itertools import combinations


class DetectSquares:
    def __init__(self):
        self.points = []

    def add(self, point):
        self.points.append(tuple(point))

    def count(self, point):
        q = tuple(point)
        total = 0
        for a, b, c in combinations(self.points, 3):
            pts = {q, a, b, c}
            if len(pts) != 4 or len([a, b, c]) != 3:
                continue
            xs = sorted({p[0] for p in (q, a, b, c)})
            ys = sorted({p[1] for p in (q, a, b, c)})
            if len(xs) == 2 and len(ys) == 2 and xs[1] - xs[0] == ys[1] - ys[0]:
                total += 1
        return total
'''),
]
