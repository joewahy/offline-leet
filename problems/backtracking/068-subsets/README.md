# 68. Subsets (Medium)

Given a list `nums` of distinct integers, return every possible subset (the power set), including the empty subset and `nums` itself. The subsets, and the numbers inside each subset, may be in any order. No subset may appear twice.

## Examples

```
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Input:  nums = [7]
Output: [[], [7]]
```

## Constraints

- `1 <= len(nums) <= 10`
- `-10 <= nums[i] <= 10`
- All values are distinct.

## Hints

- For each number you have two choices: include it or skip it.
