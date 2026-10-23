# 115. Target Sum (Medium)

You are given a list of non-negative integers `nums` and an integer `target`. Put a `+` or a `-` in front of every number, then add them up.

Return the number of different sign assignments whose total equals `target`.

## Examples

```
Input:  nums = [2, 2, 2], target = 2
Output: 3          # +2+2-2, +2-2+2, -2+2+2

Input:  nums = [1, 1, 1, 1, 1], target = 3
Output: 5
```

## Constraints

- `1 <= len(nums) <= 20`
- `0 <= nums[i] <= 1000`, and `sum(nums) <= 1000`
- `-1000 <= target <= 1000`

## Hints

- Track how many ways each running total can be reached. The totals form a small dictionary.
- Or turn it into "how many subsets sum to `(total + target) / 2`".
