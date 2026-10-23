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

- `1 <= rows, cols <= 60`
- Cells are `-1`, `0` or `2147483647`.

## Hints

- Start a breadth-first search from all gates at the same time. The first time the search reaches a room is its shortest distance.
