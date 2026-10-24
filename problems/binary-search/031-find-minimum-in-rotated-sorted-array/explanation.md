### Approach

Compare the middle element with the last one. If the middle is larger, the drop where the list wraps around must be to its right, so the minimum is in `mid + 1 .. hi`. Otherwise the middle could itself be the minimum, so keep it and search `lo .. mid`. When the range shrinks to one element, that is the minimum.

### Complexity

- Time: O(log n).
- Space: O(1).

### Watch out

Compare against `nums[hi]`, not `nums[lo]`. Against the last element the test works even when the list was not rotated at all.
