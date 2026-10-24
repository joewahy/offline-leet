# 7. Product of Array Except Self (Medium)

Given an integer list `nums`, return a list `output` where `output[i]` is the product of every element of `nums` except `nums[i]`.

Solve it in O(n) time without using division.

## Examples

```
Input:  nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]

Input:  nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]
```

## Constraints

- `2 <= len(nums) <= 10^5`
- `-20 <= nums[i] <= 20` for the small cases; products of any prefix or suffix fit in a 32-bit integer.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Division is not allowed, and zeros would break it anyway. Think about what is to the left of each position and what is to the right.
2. The answer for index `i` is (product of everything left of `i`) times (product of everything right of `i`). Build the left products in one pass.
3. Fill the output with prefix products going right, then walk from the end with a running suffix product and multiply it into the output. That uses O(n) time and O(1) extra space.

</details>
