# 34. Median of Two Sorted Arrays (Hard)

`nums1` and `nums2` are two lists of integers, each sorted in ascending order. Return the median of all their values combined (the middle value, or the average of the two middle values when the total count is even).

Your solution must run in O(log(min(m, n))) time.

## Examples

```
Input:  nums1 = [1, 2], nums2 = [3]
Output: 2.0

Input:  nums1 = [1, 3], nums2 = [2, 4]
Output: 2.5
```

## Constraints

- `0 <= len(nums1), len(nums2) <= 10000`
- `1 <= len(nums1) + len(nums2)`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Hints

- Binary search how many elements of the smaller array belong to the left half of the merged order.
- A split is correct when everything on the left is `<=` everything on the right.
