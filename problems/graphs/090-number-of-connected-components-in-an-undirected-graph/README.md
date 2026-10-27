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

- `1 <= n <= 10^5`
- `0 <= len(edges) <= 10^5`
- There are no duplicate edges and no self-loops.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Each connected group of nodes counts once. How do you avoid counting a group twice?
2. Either traverse the graph and count how many times you start a new traversal, or use union-find.
3. With union-find, start with `n` components and subtract one every time an edge joins two different components. Path compression keeps it fast.

</details>
