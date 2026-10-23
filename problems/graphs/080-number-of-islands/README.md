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

## Hints

- Scan the grid. When you meet unvisited land, count one island and flood-fill all of it (DFS or BFS).
