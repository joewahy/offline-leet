# 69. Combination Sum (Medium)

`nums` holds distinct positive integers and `target` is a positive integer. Return every unique combination of numbers from `nums` that adds up to `target`. The same number may be used any number of times. Two combinations are different if they use some number a different number of times.

The combinations, and the numbers inside each one, may be returned in any order.

## Examples

```
Input:  nums = [2, 5, 6, 9], target = 9
Output: [[2, 2, 5], [9]]

Input:  nums = [3, 4, 5], target = 16
Output: [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]
```

## Constraints

- `1 <= len(nums) <= 20`
- `2 <= nums[i] <= 30`, all distinct
- `2 <= target <= 40`
- The number of combinations is at most 150.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You may reuse a number, but the same combination in a different order must not appear twice.
2. Recurse with a start index: at each step choose a number at an index `>= start` and subtract it from the remaining target.
3. When choosing `nums[i]`, recurse with the same `i` (reuse is allowed) so you never go back to earlier numbers. Stop when the remaining target is `0` (record it) or negative (prune). Sorting lets you stop even earlier.

</details>
