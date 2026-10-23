# 80. Number of Islands (Medium)

`grid` is a map made of the strings `"1"` (land) and `"0"` (water). An island is a group of land cells connected horizontally or vertically (diagonals do not connect). Everything outside the grid counts as water.

Return the number of islands.

## Examples

```
Input:  grid = [["0","1","1","1","0"],
                ["0","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
Output: 1

Input:  grid = [["1","0"],["0","1"]]
Output: 2
```

## Constraints

- `1 <= rows, cols <= 60`
- `grid[i][j]` is `"0"` or `"1"`.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Each island is a group of connected land cells. What should you do when you find a land cell you have not seen yet?
2. Count one island, then flood fill from that cell to mark all the connected land as visited.
3. Use DFS or BFS in the four directions. Mark cells visited (a set, or overwrite with `'0'`) so each cell is processed once. The total time is O(rows * cols).

</details>
