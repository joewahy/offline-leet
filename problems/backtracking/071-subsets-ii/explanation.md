### Approach

Sort the numbers so equal values sit next to each other. Use the include/skip recursion over a starting index. Every path is a valid subset, so record it at each call. To avoid duplicate subsets, skip a number if it equals the one before it at the same level (`i > start`), because that choice has already been explored.

### Complexity

- Time: O(n * 2^n).
- Space: O(n) extra, not counting the output.

### Watch out

The condition is `i > start`, not `i > 0`. A repeated number may still be used when it follows an earlier copy in the same path.
