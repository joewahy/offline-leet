### Approach

Instead of asking, for each cell, whether water can flow to both oceans, run the flow backwards. Start at the cells touching the Pacific and climb: from a cell you may move to a neighbour that is the same height or higher. Everything reached is a cell whose water can flow to the Pacific. Do the same from the Atlantic edges. The answer is the cells in both sets.

### Complexity

- Time: O(rows * cols), two searches that visit each cell at most once.
- Space: O(rows * cols).

### Alternatives

Searching downhill from every cell would repeat the same walks many times.
