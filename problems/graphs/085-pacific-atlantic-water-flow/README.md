# 85. Pacific Atlantic Water Flow (Medium)

`heights[r][c]` is the height of a cell on an island. The Pacific Ocean touches the top and left edges of the grid, and the Atlantic Ocean touches the bottom and right edges.

Rain water can flow from a cell to a neighbouring cell (up, down, left or right) whose height is less than or equal to its own. Water on an edge cell can flow into the ocean touching that edge.

Return every cell `[r, c]` from which water can reach both oceans. The cells may be in any order.

## Examples

```
Input:  heights = [[1,2,2,3,5],
                   [3,2,3,4,4],
                   [2,4,5,3,1],
                   [6,7,1,4,5],
                   [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Constraints

- `1 <= rows, cols <= 30`
- `0 <= heights[r][c] <= 100`

## Hints

- Run the search backwards: from each ocean's edge, climb to neighbours that are the same height or higher. The answer is the intersection of the two reachable sets.
