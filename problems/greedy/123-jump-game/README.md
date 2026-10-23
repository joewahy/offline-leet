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

- `1 <= len(nums) <= 10000`
- `0 <= nums[i] <= 1000`

## Hints

- Track the farthest index you can reach so far. If you ever stand on an index beyond it, you are stuck.
