# 28. Binary Search (Easy)

`nums` is a list of distinct integers sorted in ascending order. Return the index of `target` in `nums`, or `-1` if it is not there.

Your solution should run in O(log n) time.

## Examples

```
Input:  nums = [-1, 0, 2, 4, 6, 8], target = 4
Output: 3

Input:  nums = [-1, 0, 2, 4, 6, 8], target = 3
Output: -1
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-10000 <= nums[i], target <= 10000`
- All values in `nums` are distinct.

## Hints

- Compare `target` with the middle element, and discard the half that cannot contain it.
