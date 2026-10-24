### Approach

In a binary search tree, everything left of a node is smaller and everything right is larger. Start at the root. If both `p` and `q` are smaller than the current node, the answer is in the left subtree. If both are larger, it is in the right. Otherwise the two values are on different sides, or one equals the current node, so the current node is the lowest common ancestor.

### Complexity

- Time: O(h), one step down the tree per level.
- Space: O(1), it is a loop, not a recursion.
