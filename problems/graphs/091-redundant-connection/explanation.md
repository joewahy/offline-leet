### Approach

The graph is a tree plus one extra edge, so it has exactly one cycle. Add the edges in the given order with union-find. The first edge whose two ends are already connected is the one that closes that cycle.

That is also the answer the problem wants. Any edge on the cycle could be removed, but you must return the one that appears last in the input. The cycle only exists once all of its edges have been added, so the edge that completes it is the last cycle edge in the input order.

### Complexity

- Time: O(E), nearly linear.
- Space: O(V).
