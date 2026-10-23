# 122. Maximum Subarray (Medium)

Given an integer list `nums`, find the contiguous non-empty subarray with the largest sum and return that sum.

## Examples

```
Input:  nums = [2, -3, 4, -2, 2, 1, -1, 4]
Output: 8          # 4, -2, 2, 1, -1, 4

Input:  nums = [-1]
Output: -1
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-1000 <= nums[i] <= 1000`

## Hints

- If the running sum becomes negative, it can only hurt: start a fresh subarray from the next element.
