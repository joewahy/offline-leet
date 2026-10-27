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

- `1 <= n`, and `n * n <= 10^5`
- All values in `grid` are distinct.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. For a path, the time you need is the highest elevation along it. You want the path whose highest value is smallest.
2. Search like Dijkstra, but instead of summing weights, take the maximum along the path.
3. Use a min-heap of `(max_elevation_so_far, r, c)`. Pop the smallest, and for each unvisited neighbour push `max(current, neighbour_elevation)`. When you pop the bottom-right cell, that value is the answer. Binary searching the time and checking with a BFS also works.

</details>
