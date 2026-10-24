### Approach

Inverting a tree means swapping the two children at every node. Recursively invert each child and assign the results to the opposite side. An empty node is returned as it is.

### Complexity

- Time: O(n), every node is visited once.
- Space: O(h) for the recursion, where `h` is the height of the tree. That is O(log n) for a balanced tree and O(n) for a chain.
