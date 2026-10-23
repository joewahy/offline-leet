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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The minimum is the point where the order drops. Which half of the array contains that drop?
2. Compare `nums[mid]` with `nums[right]`. If it is larger, the drop (and the minimum) is to the right of `mid`.
3. If `nums[mid] > nums[right]` set `left = mid + 1`, otherwise set `right = mid` (keep `mid`, as it may be the minimum). Stop when `left == right`.

</details>
