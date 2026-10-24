### Approach

Signals travel along edges at different costs, so this is a shortest-path problem with non-negative weights. Use Dijkstra's algorithm from the start node: keep a min-heap of `(distance, node)`, and the first time a node is popped, its distance is final. The delay is the largest of those final distances, and if some node was never reached, the answer is -1.

### Complexity

- Time: O(E log V).
- Space: O(V + E).

### Watch out

A node can be pushed onto the heap more than once. Skip any that were already finalized when popped.
