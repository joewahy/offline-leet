### Approach

A graph with `n` nodes is a tree when it is connected and has no cycle, which is the same as having exactly `n - 1` edges and no cycle. Union-find detects cycles: for each edge, find the roots of its two ends. If they are already the same, this edge closes a cycle, so the graph is not a tree. Otherwise join the two groups. At the end, the edge count must be `n - 1`.

### Complexity

- Time: O(V + E), nearly linear because of path compression.
- Space: O(V).
