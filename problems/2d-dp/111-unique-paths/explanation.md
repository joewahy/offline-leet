### Approach

Every cell can only be reached from the cell above or the cell to the left, so the number of paths to a cell is the sum of the two. The first row and column each have exactly one path. Keep just one row and update it left to right, since each cell needs only itself (the cell above) and its left neighbour.

### Complexity

- Time: O(m * n).
- Space: O(n).

### Alternatives

The answer is also the binomial coefficient `C(m + n - 2, m - 1)`, which can be computed in O(min(m, n)).
