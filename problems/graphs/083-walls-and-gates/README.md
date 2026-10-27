# 83. Walls and Gates (Medium)

`rooms` is a grid where each cell is one of:

- `-1`: a wall you cannot pass,
- `0`: a gate,
- `2147483647` (called INF): an empty room.

Fill every empty room with the number of steps to its nearest gate (moving up, down, left or right through non-wall cells). If a room cannot reach any gate, leave it as `2147483647`. Modify `rooms` in place; return nothing.

## Examples

```
Input:  [[INF, -1,  0, INF],
         [INF, INF, INF, -1],
         [INF, -1, INF, -1],
         [  0, -1, INF, INF]]
Output: [[3, -1, 0, 1],
         [2,  2, 1, -1],
         [1, -1, 2, -1],
         [0, -1, 3, 4]]
```

## Constraints

- `1 <= rows, cols`, and `rows * cols <= 10^5`
- Cells are `-1`, `0` or `2147483647`.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A distance to the 'nearest gate' is a shortest path. What search finds shortest paths in an unweighted grid?
2. Breadth-first search. Instead of starting from each empty room, start from all the gates together.
3. Put every gate in the queue at distance 0. Pop a cell and, for each neighbour that is still `2147483647`, set it to `dist + 1` and enqueue it. Walls are never entered, and each cell is set only once.

</details>
