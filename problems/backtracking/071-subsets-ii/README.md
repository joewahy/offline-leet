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

## Hints

- Sort first. When you skip a value at some position, skip all of its equal neighbours too.
