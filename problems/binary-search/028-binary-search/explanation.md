### Approach

The list is sorted, so look at the middle element. If it equals the target you are done. If it is smaller, the target can only be in the right half. If it is larger, only in the left half. Each step halves the range.

### Complexity

- Time: O(log n).
- Space: O(1).

### Watch out

Use `lo <= hi` and move the bounds to `mid + 1` and `mid - 1`. Using `mid` for both bounds can loop forever on a range of two.
