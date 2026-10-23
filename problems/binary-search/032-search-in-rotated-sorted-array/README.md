# 32. Search in Rotated Sorted Array (Medium)

A list `nums` of distinct integers, originally sorted ascending, has been rotated at an unknown pivot (for example `[0, 1, 2, 4, 5, 6, 7]` may become `[4, 5, 6, 7, 0, 1, 2]`).

Return the index of `target` in `nums`, or `-1` if it is absent. Your solution must run in O(log n) time.

## Examples

```
Input:  nums = [3, 4, 5, 6, 1, 2], target = 1
Output: 4

Input:  nums = [3, 5, 6, 0, 1, 2], target = 4
Output: -1
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-10000 <= nums[i], target <= 10000`
- All values are distinct.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. After splitting at the middle, at least one half is still in normal sorted order. How can you tell which?
2. Compare `nums[left]` with `nums[mid]`: if `nums[left] <= nums[mid]`, the left half is sorted; otherwise the right half is.
3. Check whether `target` lies inside the sorted half's range. If yes, search that half; if not, search the other half. Repeat until found, in O(log n).

</details>
