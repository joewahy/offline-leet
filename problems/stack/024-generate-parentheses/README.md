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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Build the string one character at a time. At each step, which characters are allowed?
2. You may add `(` if fewer than `n` have been used, and `)` if the number of `)` is less than the number of `(`.
3. Use backtracking with counts `opens` and `closes`. When the string reaches length `2n`, record it. Every string you reach is valid, so no work is wasted.

</details>
