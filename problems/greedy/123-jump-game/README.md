# 123. Jump Game (Medium)

You start at the first index of `nums`. `nums[i]` is the maximum number of positions you can jump forward from index `i` (you may also jump less).

Return `True` if you can reach the last index, otherwise `False`.

## Examples

```
Input:  nums = [1, 2, 0, 1, 0]
Output: True

Input:  nums = [1, 2, 1, 0, 1]
Output: False
```

## Constraints

- `1 <= len(nums) <= 10^5`
- `0 <= nums[i] <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You do not have to find the exact jumps, only whether the end is reachable.
2. Track the farthest index you can reach so far.
3. Scan left to right. If your index is beyond the farthest reach, return false. Otherwise update `reach = max(reach, i + nums[i])`. If you finish the scan, return true.

</details>
