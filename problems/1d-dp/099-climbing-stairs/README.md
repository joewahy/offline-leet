# 99. Climbing Stairs (Easy)

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
