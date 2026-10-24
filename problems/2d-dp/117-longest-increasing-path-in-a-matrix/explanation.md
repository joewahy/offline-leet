### Approach

From each cell, the longest increasing path continues into any neighbour with a larger value. Because values must strictly increase, no cell can be revisited on one path, so there are no cycles. Compute the longest path starting at each cell with recursion, and remember the result so each cell is solved only once. The answer is the maximum over all cells.

### Complexity

- Time: O(rows * cols), every cell is computed once, with four neighbour checks.
- Space: O(rows * cols) for the memo and the recursion.

### Watch out

Without the memo, the same cells are explored again and again and it becomes exponential.
