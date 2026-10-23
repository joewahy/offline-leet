# 150. Reverse Integer (Medium)

Given a signed 32-bit integer `x`, return `x` with its decimal digits reversed (keeping the sign). If the reversed value does not fit in a signed 32-bit integer (outside `[-2^31, 2^31 - 1]`), return `0`.

## Examples

```
Input:  x = 123
Output: 321

Input:  x = -123
Output: -321

Input:  x = 1534236469
Output: 0          # the reverse overflows
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Hints

- Peel digits off with `% 10` and `// 10`, handling the sign separately, and check for overflow before returning.
