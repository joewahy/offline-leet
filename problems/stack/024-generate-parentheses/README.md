# 24. Generate Parentheses (Medium)

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
