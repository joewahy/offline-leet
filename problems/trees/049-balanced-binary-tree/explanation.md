### Approach

A tree is balanced when, at every node, the two subtree heights differ by at most 1. Computing the height at each node separately would repeat work. Instead, compute heights bottom up and return -1 as soon as any subtree is unbalanced, which passes the failure straight up without looking at the rest.

### Complexity

- Time: O(n), each node is visited once.
- Space: O(h), the recursion depth.
