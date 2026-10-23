# 117. Longest Increasing Path in a Matrix (Hard)

`matrix` is a grid of integers. From any cell you may move up, down, left or right (not diagonally, and not outside the grid).

Return the length of the longest path in which every step goes to a strictly larger value.

## Examples

```
Input:  matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
Output: 4          # 1 -> 2 -> 6 -> 9

Input:  matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
Output: 4          # 3 -> 4 -> 5 -> 6
```

## Constraints

- `1 <= rows, cols <= 50`
- `0 <= matrix[i][j] <= 10^4`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. From a cell, the longest path never depends on how you arrived there, because you only move to larger values.
2. Use DFS from every cell, and remember the answer for each cell so you compute it only once (memoization).
3. `longest(r, c) = 1 + max(longest(neighbour))` over neighbours with a larger value, or `1` if there are none. Strictly increasing paths cannot loop, so caching is safe. The total time is O(rows * cols).

</details>
