### Approach

You may move as soon as the water reaches the higher of two cells, so the time to reach the end is the smallest possible value of the largest cell along a path. That is a shortest-path problem where the cost of a path is its maximum instead of its sum. Dijkstra works for it: always expand the cell with the lowest time so far, and the time of a neighbour is the larger of the current time and its own height.

The first time the bottom-right cell is popped, its time is the answer.

### Complexity

- Time: O(n^2 log n) for an n x n grid.
- Space: O(n^2).

### Alternatives

Binary searching the answer and checking with a flood fill, or adding cells in height order with union-find, are other ways to solve it.
