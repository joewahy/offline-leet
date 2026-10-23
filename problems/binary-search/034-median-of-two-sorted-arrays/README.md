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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Merging both arrays and taking the middle is O(m + n). To do better you cannot look at every element.
2. Binary search how many elements of the smaller array belong in the left half of the merged order. The rest of the left half comes from the other array.
3. A split is right when `maxLeftA <= minRightB` and `maxLeftB <= minRightA` (use infinity for empty sides). Then the median comes from those four values: the larger left value, and for an even total also the smaller right value.

</details>
