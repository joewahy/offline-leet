### Approach

Sort the candidates, then backtrack over a starting index. Each number may be used once, so recurse on `i + 1`. Stop looking along a branch once a number exceeds the remaining target, since the rest are larger. To avoid repeated combinations, skip a number that equals the previous one at the same level.

### Complexity

- Time: O(2^n) in the worst case.
- Space: O(n) extra, not counting the output.

### Watch out

The `break` on `nums[i] > remaining` is only valid because the list is sorted. It prunes everything after it.
