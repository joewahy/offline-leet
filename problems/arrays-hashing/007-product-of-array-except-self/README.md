# 7. Product of Array Except Self (Medium)

Given an integer list `nums`, return a list `output` where `output[i]` is the product of every element of `nums` except `nums[i]`.

Solve it in O(n) time without using division.

## Examples

```
Input:  nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]

Input:  nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]
```

## Constraints

- `2 <= len(nums) <= 10000`
- `-20 <= nums[i] <= 20` for the small cases; products of any prefix or suffix fit in a 32-bit integer.

## Hints

- Think of "everything to the left of i" multiplied by "everything to the right of i".
- You can build both with two passes over the list.
