# 71. Subsets II (Medium)

`nums` may contain duplicate integers. Return every possible subset, but with no duplicate subsets (two subsets are the same if they contain the same values the same number of times). The subsets, and the numbers inside them, may be in any order.

## Examples

```
Input:  nums = [1, 2, 1]
Output: [[], [1], [1, 2], [1, 1], [1, 1, 2], [2]]

Input:  nums = [7, 7]
Output: [[], [7], [7, 7]]
```

## Constraints

- `1 <= len(nums) <= 10`
- `-10 <= nums[i] <= 10`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. With duplicates, skipping 'the first 2' and skipping 'the second 2' give the same subset. How do you stop that?
2. Sort the numbers so equal values are next to each other, then use a start index when recursing.
3. In the loop over candidates at one recursion level, skip `nums[i]` if `i > start` and `nums[i] == nums[i - 1]`. That keeps each distinct subset exactly once.

</details>
