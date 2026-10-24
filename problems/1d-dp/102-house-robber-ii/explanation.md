### Approach

The first and last houses are neighbours, so you cannot rob both. That leaves two cases: rob from houses `0..n-2`, or from houses `1..n-1`. Each is the plain House Robber problem on a line, and the answer is the better of the two. A single house is a special case, because the two ranges would be empty.

### Complexity

- Time: O(n).
- Space: O(1) extra. The slices copy the list, so O(n) if you count that.
