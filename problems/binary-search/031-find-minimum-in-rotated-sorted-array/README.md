# 31. Find Minimum in Rotated Sorted Array (Medium)

A list of distinct integers that was sorted in ascending order has been rotated: some number of elements were moved from the front to the back. For example `[1, 2, 3, 4, 5]` rotated by 2 becomes `[3, 4, 5, 1, 2]`.

Given the rotated list `nums`, return its minimum element in O(log n) time.

## Examples

```
Input:  nums = [3, 4, 5, 6, 1, 2]
Output: 1

Input:  nums = [4, 5, 6, 7]
Output: 4
```

## Constraints

- `1 <= len(nums) <= 10000`
- `-10000 <= nums[i] <= 10000`
- All values are distinct. A rotation of 0 is possible.

## Hints

- Compare the middle element with the last element to see which half contains the drop.
