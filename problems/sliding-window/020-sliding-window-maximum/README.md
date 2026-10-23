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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Recomputing `max` for every window works but is slow. Which elements could never be the maximum of any future window?
2. If a newer element is larger than an older one in the window, the older one can never be the maximum again. Keep candidates in decreasing order.
3. Use a deque of indices with decreasing values. Before pushing index `i`, pop smaller values from the back; pop the front if it has left the window. The front is the maximum, and the total work is O(n).

</details>
