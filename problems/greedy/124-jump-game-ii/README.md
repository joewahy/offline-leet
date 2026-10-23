# 124. Jump Game II (Medium)

You start at index `0` of `nums`. `nums[i]` is the maximum number of positions you can jump forward from index `i`. The last index is always reachable.

Return the minimum number of jumps needed to reach the last index.

## Examples

```
Input:  nums = [2, 4, 1, 1, 1, 1]
Output: 2

Input:  nums = [2, 1, 2, 1, 0]
Output: 2
```

## Constraints

- `1 <= len(nums) <= 10000`
- `0 <= nums[i] <= 100`, and the last index can be reached from index 0

## Hints

- Think in "levels" like a breadth-first search: each jump reaches a window of indices; the next window starts right after it.
