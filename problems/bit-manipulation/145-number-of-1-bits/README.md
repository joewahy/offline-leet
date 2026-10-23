# 145. Number of 1 Bits (Easy)

Given a positive integer `n`, return the number of `1` bits in its binary representation (also called its Hamming weight).

## Examples

```
Input:  n = 11
Output: 3          # 1011

Input:  n = 128
Output: 1
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Hints

- `n & (n - 1)` clears the lowest set bit. Count how many times you can do it before `n` becomes `0`.
