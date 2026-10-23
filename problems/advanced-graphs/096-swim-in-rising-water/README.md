# 96. Swim in Rising Water (Hard)

`grid` is an `n x n` grid of distinct integers from `0` to `n * n - 1`; `grid[r][c]` is the elevation of a square. At time `t` the water level is `t` everywhere, and you can stand on (and move between) squares whose elevation is at most `t`. Swimming between adjacent squares (up, down, left, right) takes no time.

You start at the top-left square at time `0`. Return the least time at which you can reach the bottom-right square.

## Examples

```
Input:  grid = [[0, 2], [1, 3]]
Output: 3

Input:  grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
```

## Constraints

- `1 <= n <= 40`
- All values in `grid` are distinct.

## Hints

- You are looking for the path whose highest square is as low as possible. A Dijkstra-style search with a min-heap on elevation does it.
