### Approach

Do a level-order traversal and keep the last node of every level, since that is the one you would see from the right. Before processing a level, the last element of the queue is its rightmost node.

### Complexity

- Time: O(n).
- Space: O(w), the widest level.

### Alternatives

A depth-first search that visits the right child first and records the first node it sees at each new depth gives the same view with O(h) space.
