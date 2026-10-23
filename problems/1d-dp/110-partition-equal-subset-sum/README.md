# 110. Partition Equal Subset Sum (Medium)

Given a list of positive integers `nums`, return `True` if it can be split into two groups with exactly the same sum, otherwise `False`. Every number must go into exactly one group.

## Examples

```
Input:  nums = [1, 2, 3, 4]
Output: True       # [1, 4] and [2, 3]

Input:  nums = [1, 2, 3, 5]
Output: False
```

## Constraints

- `1 <= len(nums) <= 100`
- `1 <= nums[i] <= 100`

## Hints

- If the total is odd, it is impossible. Otherwise ask: can some subset add up to `total / 2`?
- Track the set of reachable sums as you go through the numbers.
