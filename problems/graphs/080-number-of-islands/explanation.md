### Approach

Scan the grid. Each time you find a land cell that has not been visited, you have found a new island: count it, then flood-fill from that cell to mark every connected land cell as visited so it is not counted again. The flood fill here uses an explicit stack and a set of visited cells.

### Complexity

- Time: O(rows * cols), each cell is visited a constant number of times.
- Space: O(rows * cols) for the visited set and the stack.

### Alternatives

A recursive DFS is shorter but can hit the recursion limit on a large island. Overwriting visited cells with `"0"` removes the visited set, at the price of changing the input.
