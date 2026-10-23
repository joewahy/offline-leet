# 81. Max Area of Island (Medium)

`grid` is a map of `1` (land) and `0` (water). An island is a group of land cells connected horizontally or vertically. Its area is the number of cells it contains.

Return the largest island area. If there is no land, return `0`.

## Examples

```
Input:  grid = [[0,1,1,0,1],
                [1,0,1,0,1],
                [0,1,1,0,1],
                [0,1,0,0,1]]
Output: 6

Input:  grid = [[0,0,0]]
Output: 0
```

## Constraints

- `1 <= rows, cols <= 60`
- `grid[i][j]` is `0` or `1`.

## Hints

- Flood-fill each island and count the cells you visit; keep the maximum.
