# 90. Number of Connected Components in an Undirected Graph (Medium)

A graph has `n` nodes labelled `0` to `n - 1` and a list of undirected `edges`, where `edges[i] = [a, b]`.

Return the number of connected components: groups of nodes that can reach each other through edges.

## Examples

```
Input:  n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Output: 2

Input:  n = 3, edges = []
Output: 3
```

## Constraints

- `1 <= n <= 5000`
- `0 <= len(edges) <= 5000`
- There are no duplicate edges and no self-loops.

## Hints

- Union-find: start with `n` components and subtract one every time an edge joins two different components.
