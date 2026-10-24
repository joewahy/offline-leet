### Approach

Checking only a node against its parent is not enough. Every node in the left subtree must be smaller than all its ancestors on the right side, and the other way around. So pass a valid range `(low, high)` down the recursion. Going left, the current value becomes the new upper bound. Going right, it becomes the new lower bound. A node outside its range makes the tree invalid.

### Complexity

- Time: O(n).
- Space: O(h), the recursion depth.

### Watch out

The range checks are strict, so a duplicate value makes the tree invalid.
