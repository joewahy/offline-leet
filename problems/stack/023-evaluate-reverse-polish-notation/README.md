# 23. Evaluate Reverse Polish Notation (Medium)

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

- `1 <= len(tokens) <= 10^5`
- Every token is an operator or an integer in the range `[-1000, 1000]`.
- Intermediate results fit in a 32-bit signed integer.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Operands wait until their operator arrives. Which data structure holds things that are waiting?
2. Push numbers onto a stack. On an operator, pop the top two values, apply it, and push the result.
3. Pop `b` first, then `a`, and compute `a op b` (the order matters for `-` and `/`). Division truncates toward zero, so use `int(a / b)` rather than `//`.

</details>
