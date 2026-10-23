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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The first and last houses are neighbours. What does that stop you from doing?
2. You cannot rob both of them. So the answer is the better of two plain House Robber problems.
3. Solve House Robber on `nums[1:]` (skip the first house) and on `nums[:-1]` (skip the last house), and return the larger result. Handle a single house separately.

</details>
