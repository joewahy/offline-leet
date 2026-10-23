# 70. Permutations (Medium)

Given a list `nums` of distinct integers, return all possible orderings (permutations) of its elements. The permutations may be returned in any order.

## Examples

```
Input:  nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Input:  nums = [1]
Output: [[1]]
```

## Constraints

- `1 <= len(nums) <= 6`
- `-10 <= nums[i] <= 10`, all distinct

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A permutation fills positions one by one. What choices does each position have?
2. At each position, pick any number not yet used, then recurse for the next position.
3. Track the used numbers (a set, a boolean list, or by removing them from a remaining list). When the path has `len(nums)` items, record a copy of it. There are `n!` results.

</details>
