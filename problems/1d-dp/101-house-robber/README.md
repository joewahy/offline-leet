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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. At each house you either rob it or skip it. What does robbing it rule out?
2. Let `best(i)` be the most you can get from the first `i` houses. It is the larger of skipping house `i` or robbing it.
3. `best(i) = max(best(i-1), best(i-2) + nums[i])`. You only need the last two values, so two variables give O(1) space.

</details>
