### Approach

The same flood fill as Number of Islands, but count how many cells each fill visits. The area of an island is the number of cells popped during its fill, and the answer is the largest one.

### Complexity

- Time: O(rows * cols).
- Space: O(rows * cols) for the visited set and the stack.
