# 107. Maximum Product Subarray (Medium)

Given an integer list `nums`, return the largest product of any non-empty contiguous subarray.

## Examples

```
Input:  nums = [1, 2, -3, 4]
Output: 4

Input:  nums = [-2, 3, -4]
Output: 24
```

## Constraints

- `1 <= len(nums) <= 1000`
- `-10 <= nums[i] <= 10`
- The answer fits in a 32-bit integer for the checked tests.

## Hints

- A negative number can turn the smallest product into the largest. Track both the maximum and the minimum product ending at each position.
