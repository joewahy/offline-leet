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

## Hints

- Choose any unused number for the first position, then recurse on the rest.
