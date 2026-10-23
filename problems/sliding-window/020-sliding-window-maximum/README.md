# 20. Sliding Window Maximum (Hard)

A window of size `k` slides from the left end of `nums` to the right end, one position at a time. Return a list holding the maximum value inside the window at each position.

## Examples

```
Input:  nums = [1, 2, 1, 0, 4, 2, 6], k = 3
Output: [2, 2, 4, 4, 6]

Input:  nums = [9, 11], k = 2
Output: [11]
```

## Constraints

- `1 <= k <= len(nums) <= 10000`
- `-10000 <= nums[i] <= 10000`

## Hints

- A deque of indices, kept in decreasing order of value, gives each maximum in amortised O(1).
