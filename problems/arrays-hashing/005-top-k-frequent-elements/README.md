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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You need two things: how often each number appears, and which `k` counts are the largest.
2. Count with a dictionary, then either sort by count, keep a min-heap of size `k`, or use buckets indexed by frequency.
3. Bucket sort gives O(n): a frequency is at most `len(nums)`, so make a list of that size where index `f` holds the numbers that appear `f` times, then read it from the end.

</details>
