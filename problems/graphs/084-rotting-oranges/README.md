# 84. Rotting Oranges (Medium)

`grid` describes a box of oranges: `0` is an empty cell, `1` is a fresh orange, and `2` is a rotten orange.

Every minute, each fresh orange that is directly next to a rotten one (up, down, left or right) becomes rotten.

Return the number of minutes until no fresh orange is left. If that never happens, return `-1`.

## Examples

```
Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
```

## Constraints

- `1 <= rows, cols <= 60`
- `grid[i][j]` is `0`, `1` or `2`.

## Hints

- Spread rot one minute at a time with a breadth-first search that starts from every rotten orange.
- At the end, check whether any fresh orange remains.
