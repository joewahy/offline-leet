### Approach

The depth of a tree is 1 plus the depth of its deeper child, and an empty tree has depth 0. The recursion follows that definition directly.

### Complexity

- Time: O(n).
- Space: O(h), the recursion depth.

### Alternatives

A breadth-first search level by level, counting the levels, gives the same answer with O(w) space, where `w` is the widest level, and no deep recursion.
