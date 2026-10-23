# 140. Plus One (Easy)

A non-negative integer is stored as a list of its decimal `digits`, most significant digit first, with no leading zeros (except the number `0` itself). Add one to the integer and return the resulting list of digits.

## Examples

```
Input:  digits = [1, 2, 3]
Output: [1, 2, 4]

Input:  digits = [9, 9]
Output: [1, 0, 0]
```

## Constraints

- `1 <= len(digits) <= 100`
- `0 <= digits[i] <= 9`

## Hints

- Work from the last digit. A `9` becomes `0` and carries; stop at the first digit that is not `9`.
