### Approach

Walk the list once and point each node back at the node before it. Keep `prev`, the already reversed part. For each node, save its old `next`, set its `next` to `prev`, then step forward. When you run off the end, `prev` is the new head.

### Complexity

- Time: O(n).
- Space: O(1).

### Alternatives

The recursive version reverses the rest of the list and then fixes the first node. It is the same time but uses O(n) stack space, and it hits the recursion limit on long lists.
