### Approach

The longest path through a node goes down its left side and down its right side, so its length is `left height + right height`. The longest path in the tree is the best of that over all nodes. Compute heights recursively, and at each node update the best answer before returning the node's own height (`1 + max(left, right)`).

### Complexity

- Time: O(n), each node is visited once.
- Space: O(h), the recursion depth.

### Watch out

The longest path does not have to pass through the root, which is why it is checked at every node.
