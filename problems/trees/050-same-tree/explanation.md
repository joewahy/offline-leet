### Approach

Two trees are the same if they are both empty, or if their roots have equal values and their left subtrees match and their right subtrees match. If exactly one is empty, or the values differ, they are not the same.

### Complexity

- Time: O(n), where `n` is the size of the smaller tree, since the walk stops at the first difference.
- Space: O(h), the recursion depth.
