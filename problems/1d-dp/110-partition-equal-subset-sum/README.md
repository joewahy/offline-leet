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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If the total is odd, can the two halves be equal? If it is even, what exactly are you looking for?
2. You need a subset that sums to `total / 2`. That is a subset-sum problem.
3. Keep the set of reachable sums (or a boolean array up to `total / 2`). For each number, add it to every reachable sum. If `total / 2` becomes reachable, return true. A bitmask `reach |= reach << x` does it compactly.

</details>
