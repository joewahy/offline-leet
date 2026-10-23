# 12. 3Sum (Medium)

Given a list of integers `nums`, return every distinct triplet `[a, b, c]` of values taken from three different positions such that `a + b + c == 0`.

The same combination of values must not appear twice in the answer. The triplets and the numbers inside them may be returned in any order.

## Examples

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Input:  nums = [0, 1, 1]
Output: []
```

## Constraints

- `3 <= len(nums) <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Hints

- Sort first. Fix one number, then look for the other two with two pointers.
- Skip equal neighbours to avoid duplicate triplets.
