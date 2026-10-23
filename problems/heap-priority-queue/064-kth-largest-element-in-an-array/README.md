# 64. Kth Largest Element in an Array (Medium)

Given an integer list `nums` and an integer `k`, return the `k`-th largest element in sorted order (not the `k`-th distinct element).

## Examples

```
Input:  nums = [2, 3, 1, 5, 4], k = 2
Output: 4

Input:  nums = [2, 3, 1, 1, 5, 5, 4], k = 3
Output: 4
```

## Constraints

- `1 <= k <= len(nums) <= 10000`
- `-10000 <= nums[i] <= 10000`

## Hints

- Sorting is O(n log n). A min-heap of size `k` or quickselect can do better.
