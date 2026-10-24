### Approach

Write the tree in preorder, using `N` for a missing child, with commas between values. Preorder with markers has only one possible reading, so `deserialize` can rebuild the tree by reading tokens in order: a `N` is an empty subtree, and any number is a node whose left and right subtrees come next.

The serializer uses an explicit stack, pushing the right child before the left so the left is processed first.

### Complexity

- Time: O(n) for both directions.
- Space: O(n) for the string and the stack.

### Alternatives

A level-order encoding (the format LeetCode shows) works as well. It uses a queue instead of recursion.
