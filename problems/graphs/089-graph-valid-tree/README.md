# 89. Graph Valid Tree (Medium)

A graph has `n` nodes labelled `0` to `n - 1` and a list of undirected `edges`, where `edges[i] = [a, b]`.

Return `True` if the edges form a valid tree (connected, with no cycles), otherwise `False`.

## Examples

```
Input:  n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: True

Input:  n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: False
```

## Constraints

- `1 <= n <= 3000`
- `0 <= len(edges) <= 3000`
- There are no duplicate edges and no self-loops.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. What two properties define a tree? How many edges does it have, and what must be true about its connectivity?
2. A tree on `n` nodes has exactly `n - 1` edges and is connected (equivalently, it has no cycle).
3. Check `len(edges) == n - 1` first. Then verify connectivity with a DFS from node 0, or add the edges with union-find and fail if an edge joins two nodes that are already connected.

</details>
