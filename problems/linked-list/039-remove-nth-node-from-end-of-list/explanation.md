### Approach

Use two pointers, `lead` and `trail`. Move `lead` forward `n` nodes first, so the gap between them is `n`. Then move both until `lead` is at the last node. At that point `trail` is just before the node to remove, so skip it with `trail.next = trail.next.next`.

A dummy node in front of the head handles the case where the head itself is removed.

### Complexity

- Time: O(n), a single pass.
- Space: O(1).

### Alternatives

Counting the length first and then walking to the right spot takes two passes. It is also O(n) and a little simpler.
