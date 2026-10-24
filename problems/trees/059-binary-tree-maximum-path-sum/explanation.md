### Approach

A path can turn at most once, so the best path has a highest node with a branch down each side. For each node, compute the best gain it can offer its parent, which is its own value plus the better of its two branches. Branches with a negative gain are replaced by 0, since it is better to leave them out. While doing that, the best path that turns at this node, `value + left + right`, updates the overall answer.

### Complexity

- Time: O(n).
- Space: O(h), the recursion depth.

### Watch out

The answer starts at negative infinity, not 0, because a tree of all negative values still has to return its largest single node.
