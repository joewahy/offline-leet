### Approach

At any midpoint, at least one half of the range is sorted. Check which one by comparing `nums[lo]` with `nums[mid]`. Then see whether the target lies inside that sorted half: if it does, search that half, and if it does not, search the other half. Each step discards half the range.

### Complexity

- Time: O(log n).
- Space: O(1).

### Watch out

The inequalities at the ends matter. The sorted-half checks include the end values (`nums[lo] <= target`, `target <= nums[hi]`), while `mid` was already tested for equality at the top of the loop.
