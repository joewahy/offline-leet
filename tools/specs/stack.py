from spec import P

CATEGORY = "stack"

_PAIRS = {"(": ")", "[": "]", "{": "}"}


def _balanced(rng, n_pairs):
    out, stack = [], []
    opens = n_pairs
    while opens or stack:
        if opens and (not stack or rng.random() < 0.5):
            c = rng.choice("([{")
            out.append(c)
            stack.append(c)
            opens -= 1
        else:
            out.append(_PAIRS[stack.pop()])
    return "".join(out)


def _paren_gen(rng):
    out = [[_balanced(rng, rng.randint(1, 6))] for _ in range(3)]
    out += [["".join(rng.choice("()[]{}") for _ in range(rng.randint(1, 10)))] for _ in range(3)]
    s = _balanced(rng, 4000)
    out += [[s], [s[:-1] + "("], [s[:2000] + s[2001:]], ["(" * 5000 + ")" * 5000], ["(" * 5000 + ")" * 4999 + "]"]]
    return out


def _min_stack_ops(rng, n):
    ops, params, size = ["MinStack"], [[]], 0
    for _ in range(n):
        r = rng.random()
        if size == 0 or r < 0.45:
            ops.append("push")
            params.append([rng.randint(-20, 20)])
            size += 1
        elif r < 0.65:
            ops.append("pop")
            params.append([])
            size -= 1
        else:
            ops.append(rng.choice(["top", "getMin"]))
            params.append([])
    return [ops, params]


def _rpn(rng, steps):
    tokens, stack = [], []
    for _ in range(steps):
        if len(stack) < 2 or rng.random() < 0.55:
            v = rng.randint(-30, 30)
            tokens.append(str(v))
            stack.append(v)
            continue
        b, a = stack.pop(), stack.pop()
        op = rng.choice("+-*/")
        if op == "/" and b == 0:
            op = "+"
        if op == "*" and abs(a * b) > 10**6:
            op = "-"
        v = {"+": a + b, "-": a - b, "*": a * b, "/": (abs(a) // abs(b)) * (1 if (a < 0) == (b < 0) else -1) if op == "/" else 0}[op]
        tokens.append(op)
        stack.append(v)
    while len(stack) > 1:
        stack.pop()
        stack.pop()
        stack.append(0)
        tokens.append("+")
    return tokens


def _fleet(rng, n, target, vmax):
    pos = rng.sample(range(target), n)
    return [target, pos, [rng.randint(1, vmax) for _ in range(n)]]


_MIN_STACK_STUB = r'''
class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass
'''

PROBLEMS = [
    P(21, "Valid Parentheses", "Easy", "isValid",
      r'''
A string `s` contains only the characters `(`, `)`, `[`, `]`, `{` and `}`. It is valid when every opening bracket is closed by the same kind of bracket, in the right order, and every closing bracket matches an earlier opening one.

Return `True` if `s` is valid, otherwise `False`.

## Examples

```
Input:  s = "[]"
Output: True

Input:  s = "([{}])"
Output: True

Input:  s = "[(])"
Output: False
```

## Constraints

- `1 <= len(s) <= 10000`

## Hints

- The most recent unmatched opening bracket must be closed first. Which data structure behaves that way?
''',
      r'''
class Solution:
    def isValid(self, s: str) -> bool:
        pass
''',
      r'''
class Solution:
    def isValid(self, s):
        match = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in match:
                if not stack or stack.pop() != match[c]:
                    return False
            else:
                stack.append(c)
        return not stack
''',
      [(["[]"], True), (["([{}])"], True), (["[(])"], False), (["("], False), ([")"], False),
       (["()[]{}"], True), (["(]"], False), (["{[]}"], True), (["(("], False), (["([)]"], False),
       (["((()))"], True), (["(){}}{"], False)],
      gen=_paren_gen,
      small=lambda rng: ["".join(rng.choice("()[]{}") for _ in range(rng.randint(1, 8)))],
      brute=r'''
class Solution:
    def isValid(self, s):
        while True:
            t = s.replace("()", "").replace("[]", "").replace("{}", "")
            if t == s:
                return s == ""
            s = t
'''),

    P(22, "Min Stack", "Medium", "MinStack",
      r'''
Design a stack that supports the usual operations and can also report its smallest element, all in O(1) time.

Implement the class `MinStack`:

- `MinStack()` creates an empty stack.
- `push(val)` pushes `val`.
- `pop()` removes the top element.
- `top()` returns the top element.
- `getMin()` returns the smallest element currently in the stack.

`pop`, `top` and `getMin` are only called when the stack is not empty.

## Examples

```
MinStack(); push(1); push(2); push(0)
getMin()  -> 0
pop()
top()     -> 2
getMin()  -> 1
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `10000` calls are made.

## Hints

- Store with each element the minimum of everything beneath it (and itself).
''',
      _MIN_STACK_STUB,
      r'''
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append((val, min(val, self.stack[-1][1]) if self.stack else val))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
''',
      [([["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], [[], [1], [2], [0], [], [], [], []]],
        [None, None, None, None, 0, None, 2, 1]),
       ([["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], [[], [-2], [0], [-3], [], [], [], []]],
        [None, None, None, None, -3, None, 0, -2]),
       ([["MinStack", "push", "getMin", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
         [[], [5], [], [5], [3], [], [], [], [], []]], [None, None, 5, None, None, 3, None, 5, None, 5]),
       ([["MinStack", "push", "top", "getMin", "pop"], [[], [7], [], [], []]], [None, None, 7, 7, None]),
       ([["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
         [[], [2], [1], [1], [], [], [], [], []]], [None, None, None, None, 1, None, 1, None, 2])],
      design="MinStack",
      gen=lambda rng: [_min_stack_ops(rng, n) for n in (20, 60, 200, 4000)],
      small=lambda rng: _min_stack_ops(rng, rng.randint(1, 15)),
      brute=r'''
class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)

    def pop(self):
        self.s.pop()

    def top(self):
        return self.s[-1]

    def getMin(self):
        return min(self.s)
'''),

    P(23, "Evaluate Reverse Polish Notation", "Medium", "evalRPN",
      r'''
`tokens` is an arithmetic expression in reverse Polish (postfix) notation: each operator comes after its two operands. The valid operators are `+`, `-`, `*` and `/`.

Evaluate the expression and return the result as an integer. Division between two integers always truncates toward zero (so `-7 / 2` is `-3`). The expression is always valid and never divides by zero.

## Examples

```
Input:  tokens = ["1", "2", "+", "3", "*", "4", "-"]
Output: 5          # ((1 + 2) * 3) - 4

Input:  tokens = ["4", "13", "5", "/", "+"]
Output: 6          # 4 + (13 / 5)
```

## Constraints

- `1 <= len(tokens) <= 10000`
- Every token is an operator or an integer in the range `[-1000, 1000]`.
- Intermediate results fit in a 32-bit signed integer.

## Hints

- Push numbers on a stack. When you see an operator, pop two, combine, and push the result.
- Mind the order of operands for `-` and `/`, and truncate toward zero with `int(a / b)`.
''',
      r'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pass
''',
      r'''
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in "+-*/" and len(t) == 1:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    q = abs(a) // abs(b)
                    stack.append(q if (a < 0) == (b < 0) else -q)
            else:
                stack.append(int(t))
        return stack[0]
''',
      [([["1", "2", "+", "3", "*", "4", "-"]], 5), ([["4", "13", "5", "/", "+"]], 6),
       ([["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]], 22),
       ([["2", "1", "+", "3", "*"]], 9), ([["18"]], 18), ([["3", "-4", "/"]], 0), ([["-7", "2", "/"]], -3),
       ([["7", "-2", "/"]], -3), ([["0", "3", "/"]], 0), ([["5", "1", "2", "+", "4", "*", "+", "3", "-"]], 14)],
      gen=lambda rng: [[_rpn(rng, n)] for n in (5, 10, 30, 400, 3000)],
      small=lambda rng: [_rpn(rng, rng.randint(1, 8))],
      brute=r'''
class Solution:
    def evalRPN(self, tokens):
        st = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                b, a = st.pop(), st.pop()
                st.append(a + b if t == "+" else a - b if t == "-" else a * b if t == "*" else int(a / b))
            else:
                st.append(int(t))
        return st[0]
'''),

    P(24, "Generate Parentheses", "Medium", "generateParenthesis",
      r'''
Given `n` pairs of parentheses, return every well-formed combination as a list of strings. The strings may be in any order.

## Examples

```
Input:  n = 1
Output: ["()"]

Input:  n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

## Constraints

- `1 <= n <= 8`

## Hints

- Build the string one character at a time. You may add `(` while fewer than `n` are used, and `)` while there are more opens than closes.
''',
      r'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass
''',
      r'''
class Solution:
    def generateParenthesis(self, n):
        out = []

        def build(cur, opens, closes):
            if len(cur) == 2 * n:
                out.append(cur)
                return
            if opens < n:
                build(cur + "(", opens + 1, closes)
            if closes < opens:
                build(cur + ")", opens, closes + 1)

        build("", 0, 0)
        return out
''',
      [([1], ["()"]), ([2], ["(())", "()()"]), ([3], ["((()))", "(()())", "(())()", "()(())", "()()()"]),
       ([4], ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())",
              "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])],
      compare="unordered",
      gen=lambda rng: [[5], [6], [7], [8]],
      small=lambda rng: [rng.randint(1, 6)],
      brute=r'''
from itertools import product


class Solution:
    def generateParenthesis(self, n):
        out = []
        for chars in product("()", repeat=2 * n):
            depth = 0
            for c in chars:
                depth += 1 if c == "(" else -1
                if depth < 0:
                    break
            else:
                if depth == 0:
                    out.append("".join(chars))
        return out
'''),

    P(25, "Daily Temperatures", "Medium", "dailyTemperatures",
      r'''
`temperatures[i]` is the temperature on day `i`. Return a list `answer` where `answer[i]` is how many days you must wait after day `i` for a warmer temperature. If no warmer day ever comes, `answer[i]` is `0`.

## Examples

```
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Input:  temperatures = [30, 38, 30, 36, 35, 40, 28]
Output: [1, 4, 1, 2, 1, 0, 0]
```

## Constraints

- `1 <= len(temperatures) <= 10000`
- `30 <= temperatures[i] <= 100`

## Hints

- Keep a stack of days still waiting for a warmer day. When a warmer day arrives, pop everything it beats.
''',
      r'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass
''',
      r'''
class Solution:
    def dailyTemperatures(self, temperatures):
        out = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                out[j] = i - j
            stack.append(i)
        return out
''',
      [([[73, 74, 75, 71, 69, 72, 76, 73]], [1, 1, 4, 2, 1, 1, 0, 0]),
       ([[30, 38, 30, 36, 35, 40, 28]], [1, 4, 1, 2, 1, 0, 0]), ([[22, 21, 20]], [0, 0, 0]), ([[30]], [0]),
       ([[30, 30]], [0, 0]), ([[30, 31]], [1, 0]), ([[31, 30, 32]], [2, 1, 0]), ([[50, 50, 50, 90]], [3, 2, 1, 0])],
      gen=lambda rng: [[[rng.randint(30, 40) for _ in range(rng.randint(1, 12))]] for _ in range(3)]
      + [[[rng.randint(30, 100) for _ in range(10000)]]]
      + [[[50] * 9999 + [90]]],
      small=lambda rng: [[rng.randint(30, 36) for _ in range(rng.randint(1, 10))]],
      brute=r'''
class Solution:
    def dailyTemperatures(self, temperatures):
        out = []
        for i, t in enumerate(temperatures):
            d = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > t:
                    d = j - i
                    break
            out.append(d)
        return out
'''),

    P(26, "Car Fleet", "Medium", "carFleet",
      r'''
Several cars drive along a one-lane road toward a destination `target` miles away. Car `i` starts at `position[i]` and drives at a constant `speed[i]` miles per hour.

A car can never overtake the car in front of it. If it catches up, it slows down and travels at the same speed right behind it. A group of cars that end up driving together is a fleet, and a lone car is also a fleet. A car that catches another exactly at the destination counts as part of that fleet.

Return the number of fleets that arrive at the destination.

## Examples

```
Input:  target = 10, position = [1, 4], speed = [3, 2]
Output: 1

Input:  target = 10, position = [4, 1, 0, 7], speed = [2, 2, 1, 1]
Output: 3
```

## Constraints

- `1 <= len(position) == len(speed) <= 10000`
- `0 <= position[i] < target <= 10^6`, all positions are distinct
- `1 <= speed[i] <= 100`

## Hints

- Sort by starting position, closest to the destination first. Compute how long each car needs to arrive on its own.
- A car joins the fleet ahead if its own time is not longer than that fleet's time.
''',
      r'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def carFleet(self, target, position, speed):
        fleets = 0
        slowest = 0.0
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if t > slowest:
                fleets += 1
                slowest = t
        return fleets
''',
      [([10, [1, 4], [3, 2]], 1), ([10, [4, 1, 0, 7], [2, 2, 1, 1]], 3),
       ([12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]], 3), ([100, [0, 2, 4], [4, 2, 1]], 1), ([10, [3], [3]], 1),
       ([10, [0, 5], [1, 1]], 2), ([20, [6, 2, 17], [3, 9, 2]], 2)],
      gen=lambda rng: [_fleet(rng, n, t, 5) for n, t in ((4, 10), (6, 30), (8, 50), (12, 100))]
      + [_fleet(rng, 10000, 1000000, 100)] + [_fleet(rng, 10000, 1000000, 3)],
      small=lambda rng: _fleet(rng, rng.randint(1, 6), 20, 4),
      brute=r'''
from fractions import Fraction


class Solution:
    def carFleet(self, target, position, speed):
        times = {p: Fraction(target - p, s) for p, s in zip(position, speed)}
        return sum(1 for p in position if all(times[p] > times[q] for q in position if q > p))
'''),

    P(27, "Largest Rectangle in Histogram", "Hard", "largestRectangleArea",
      r'''
`heights[i]` is the height of the `i`-th bar in a histogram. Every bar is 1 unit wide and the bars touch each other.

Return the area of the largest rectangle that fits entirely inside the histogram.

## Examples

```
Input:  heights = [7, 1, 7, 2, 2, 4]
Output: 8          # the bars 7, 2, 2, 4 with height 2

Input:  heights = [1, 3, 7]
Output: 7
```

## Constraints

- `1 <= len(heights) <= 8000`
- `0 <= heights[i] <= 10000`

## Hints

- For each bar, how far can a rectangle of that bar's height extend left and right?
- A stack of increasing heights finds those boundaries in one pass.
''',
      r'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        best = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx
            stack.append((start, h))
        return best
''',
      [([[7, 1, 7, 2, 2, 4]], 8), ([[1, 3, 7]], 7), ([[2, 1, 5, 6, 2, 3]], 10), ([[2, 4]], 4), ([[1]], 1),
       ([[0]], 0), ([[5, 5, 5]], 15), ([[6, 2, 5, 4, 5, 1, 6]], 12), ([[1, 1]], 2), ([[4, 2, 0, 3, 2, 5]], 6)],
      gen=lambda rng: [[[rng.randint(0, 9) for _ in range(rng.randint(1, 12))]] for _ in range(3)]
      + [[[rng.randint(0, 10000) for _ in range(8000)]]]
      + [[list(range(1, 4001)) + list(range(4000, 0, -1))]],
      small=lambda rng: [[rng.randint(0, 8) for _ in range(rng.randint(1, 9))]],
      brute=r'''
class Solution:
    def largestRectangleArea(self, heights):
        best = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                best = max(best, min(heights[i:j + 1]) * (j - i + 1))
        return best
'''),
]
