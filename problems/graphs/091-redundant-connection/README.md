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

- `3 <= n <= 10^5`, and `len(edges) == n`
- `1 <= a < b <= n` is not guaranteed; an edge may be written in either direction.
- There are no repeated edges.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The extra edge is the one that connects two nodes that were already connected.
2. Add the edges one at a time with union-find.
3. For each edge, find the roots of its endpoints. If they are the same, this edge closes a cycle, so return it. Otherwise union the two groups.

</details>
