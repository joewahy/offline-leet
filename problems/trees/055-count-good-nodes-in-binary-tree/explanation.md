### Approach

A node is good if no node on the path from the root to it has a bigger value. Pass the biggest value seen so far down the recursion. At each node, check whether it is at least that big, update the maximum for its children, and add up the good nodes in both subtrees.

### Complexity

- Time: O(n).
- Space: O(h), the recursion depth.
