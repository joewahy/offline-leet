# 91. Redundant Connection (Medium)

A connected, undirected graph with nodes labelled `1` to `n` was a tree, and then one extra edge was added. You are given the resulting list of `edges`.

Return an edge that can be removed so that the remaining graph is a tree again. If several edges qualify, return the one that appears last in `edges`.

## Examples

```
Input:  edges = [[1, 2], [1, 3], [2, 3]]
Output: [2, 3]

Input:  edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
Output: [1, 4]
```

## Constraints

- `3 <= n <= 1000`, and `len(edges) == n`
- `1 <= a < b <= n` is not guaranteed; an edge may be written in either direction.
- There are no repeated edges.

## Hints

- Add the edges one by one with union-find. The first edge whose endpoints are already connected closes the cycle.
