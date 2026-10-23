# 5. Top K Frequent Elements (Medium)

Given a list of integers `nums` and an integer `k`, return the `k` values that occur most often. The answer is guaranteed to be unique, and may be returned in any order.

## Examples

```
Input:  nums = [1, 2, 2, 3, 3, 3], k = 2
Output: [2, 3]

Input:  nums = [7, 7], k = 1
Output: [7]
```

## Constraints

- `1 <= len(nums) <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `1 <= k <=` the number of distinct values in `nums`

## Hints

- Count occurrences first.
- Sorting by count is O(n log n). Can you do better with a heap or bucket sort?
