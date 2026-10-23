# 102. House Robber II (Medium)

Same as House Robber, but the houses are arranged in a circle: the first and the last house are neighbours. Robbing two neighbouring houses sets off the alarm.

Return the largest amount of money you can rob without triggering any alarm.

## Examples

```
Input:  nums = [3, 4, 3]
Output: 4

Input:  nums = [2, 9, 8, 3, 6]
Output: 15         # 9 + 6
```

## Constraints

- `1 <= len(nums) <= 1000`
- `0 <= nums[i] <= 1000`

## Hints

- Because house 0 and the last house cannot both be robbed, solve the linear problem twice: once without the first house, once without the last.
