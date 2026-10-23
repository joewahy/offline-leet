# 101. House Robber (Medium)

`nums[i]` is the amount of money in house `i`, along a street. Houses next to each other have linked alarms: robbing two neighbouring houses sets off the alarm.

Return the largest amount of money you can rob without triggering any alarm.

## Examples

```
Input:  nums = [1, 1, 3, 3]
Output: 4          # rob house 1 and house 3

Input:  nums = [2, 9, 8, 3, 6]
Output: 16         # 2 + 8 + 6
```

## Constraints

- `1 <= len(nums) <= 10000`
- `0 <= nums[i] <= 400`

## Hints

- For each house, either skip it (best so far) or rob it (its money plus the best up to two houses back).
