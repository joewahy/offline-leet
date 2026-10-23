# 68. Subsets (Medium)

Given a list `nums` of distinct integers, return every possible subset (the power set), including the empty subset and `nums` itself. The subsets, and the numbers inside each subset, may be in any order. No subset may appear twice.

## Examples

```
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Input:  nums = [7]
Output: [[], [7]]
```

## Constraints

- `1 <= len(nums) <= 10`
- `-10 <= nums[i] <= 10`
- All values are distinct.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. For each number there are two choices. How many subsets does that give for `n` numbers?
2. Decide for each element whether to include it, and recurse on the rest. Collect the chosen elements when you reach the end.
3. Iterative form: start with `[[]]` and, for each number, add a copy of every existing subset with that number appended. The answer has `2^n` subsets.

</details>
