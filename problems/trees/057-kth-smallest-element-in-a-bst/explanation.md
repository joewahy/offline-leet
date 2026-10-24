### Approach

An in-order traversal of a binary search tree visits the values in increasing order, so the `k`-th node visited is the answer. Do the traversal with an explicit stack: push the whole left spine, pop a node, count it, then move to its right child. Stop as soon as the count reaches `k`.

### Complexity

- Time: O(h + k). It walks down to the leftmost node, then visits `k` nodes.
- Space: O(h) for the stack.

### Alternatives

Collecting the whole in-order list and indexing it is O(n) time and space.
