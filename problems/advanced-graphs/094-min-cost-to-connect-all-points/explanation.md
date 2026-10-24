### Approach

Connecting all points at the lowest total cost is a minimum spanning tree. Prim's algorithm grows it from one point: keep for each outside point the cheapest distance to the tree, repeatedly add the cheapest one, and update the other points' distances using the new point. The distance is Manhattan distance.

The graph is complete, with about n^2 edges, so a simple array version of Prim's (no heap) is just as fast as a heap version here.

### Complexity

- Time: O(n^2).
- Space: O(n).

### Alternatives

Kruskal's algorithm sorts all n^2 edges and uses union-find. It is O(n^2 log n).
