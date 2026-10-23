# 147. Reverse Bits (Easy)

Given an unsigned 32-bit integer `n`, reverse its bits (treat it as exactly 32 binary digits) and return the resulting unsigned integer.

## Examples

```
Input:  n = 3          # 00000000000000000000000000000011
Output: 3221225472     # 11000000000000000000000000000000

Input:  n = 43261596
Output: 964176192
```

## Constraints

- `0 <= n <= 2^32 - 1`

## Hints

- Build the answer one bit at a time: shift the result left, then add the lowest bit of `n`, then shift `n` right. Do this 32 times.
