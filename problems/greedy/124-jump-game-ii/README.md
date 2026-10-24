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

- `1 <= len(nums) <= 10^5`
- `0 <= nums[i] <= 100`, and the last index can be reached from index 0

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Think of each jump as moving to a new 'level' of indices, like in a BFS.
2. From the current level (the indices reachable with `j` jumps), find the farthest index you can reach with one more jump.
3. Track `end` (the end of the current level) and `far`. When you reach `i == end`, you must jump: increment the count and set `end = far`. Stop before the last index.

</details>
