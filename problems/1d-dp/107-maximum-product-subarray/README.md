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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Two negative numbers multiply to a positive. What does that do to the smallest product so far?
2. Track both the largest and the smallest product of a subarray ending at the current position.
3. At each number `x`, the new max is `max(x, hi * x, lo * x)` and the new min is `min(x, hi * x, lo * x)`, computed from the old values. The answer is the best max seen. A zero resets the run automatically.

</details>
