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

- `1 <= len(tokens) <= 10000`
- Every token is an operator or an integer in the range `[-1000, 1000]`.
- Intermediate results fit in a 32-bit signed integer.

## Hints

- Push numbers on a stack. When you see an operator, pop two, combine, and push the result.
- Mind the order of operands for `-` and `/`, and truncate toward zero with `int(a / b)`.
