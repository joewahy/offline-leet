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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Sorting the whole array works. Do you need the entire order, or just the top `k`?
2. Keep a min-heap of size `k`. After processing every number, its smallest element is the `k`-th largest.
3. Push each number; if the heap grows beyond `k`, pop the smallest. That is O(n log k). Quickselect gives O(n) on average.

</details>
