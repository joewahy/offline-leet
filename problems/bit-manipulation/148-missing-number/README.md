# 148. Missing Number (Easy)

`nums` contains `n` distinct integers taken from the range `[0, n]`, so exactly one number from that range is missing. Return it.

## Examples

```
Input:  nums = [1, 2, 3]
Output: 0

Input:  nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
```

## Constraints

- `1 <= n <= 10000`
- All numbers are distinct and between `0` and `n`.

## Hints

- The sum `0 + 1 + ... + n` is known. Or XOR every index and every value together.
