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

- `1 <= len(nums) <= 10^5`
- `-1000 <= nums[i] <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If the sum of a prefix is negative, can it help any later subarray?
2. No. A negative running sum should be thrown away and a new subarray started.
3. Keep `cur = max(x, cur + x)` and the best `cur` seen. This is Kadane's algorithm, O(n) time and O(1) space.

</details>
