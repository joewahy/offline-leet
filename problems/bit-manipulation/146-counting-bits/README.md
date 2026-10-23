# 146. Counting Bits (Easy)

Given an integer `n`, return a list `ans` of length `n + 1` where `ans[i]` is the number of `1` bits in the binary representation of `i`.

Aim for O(n) time total, by reusing results you already computed.

## Examples

```
Input:  n = 4
Output: [0, 1, 1, 2, 1]

Input:  n = 2
Output: [0, 1, 1]
```

## Constraints

- `0 <= n <= 10000`

## Hints

- `i` has the same bits as `i >> 1` plus possibly one more (its lowest bit).
