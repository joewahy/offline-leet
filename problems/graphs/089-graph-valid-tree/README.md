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

## Hints

- A tree on `n` nodes has exactly `n - 1` edges. If that holds, you only need to check one more thing.
