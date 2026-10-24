### Approach

The graph is a tree plus one extra edge. Add the edges in the given order with union-find. The first edge whose two ends are already connected is the one that creates the cycle, so it is the redundant edge. The problem asks for the last such edge in the input, and since there is only one extra edge, the first one found is the answer.

### Complexity

- Time: O(E), nearly linear.
- Space: O(V).
