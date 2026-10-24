### Approach

The first element of the preorder list is the root. In the inorder list, everything left of the root's position is the left subtree and everything right of it is the right subtree. Build recursively: take the next preorder value as the root, find its position in the inorder list, and build the left side first, then the right side.

A dictionary from value to inorder position makes each lookup O(1), and an iterator over `preorder` hands out roots in the right order because preorder visits the left subtree completely before the right.

### Complexity

- Time: O(n).
- Space: O(n) for the dictionary and the new tree.

### Alternatives

Searching the inorder list for the root each time is O(n^2) on a skewed tree.
