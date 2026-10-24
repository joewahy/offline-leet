### Approach

Try every node of `root` as a possible match. At each node, check whether the tree starting there is identical to `subRoot`, using the Same Tree check. If it is not, look for a match in the left or the right subtree.

### Complexity

- Time: O(n * m), where `m` is the size of `subRoot`. In the worst case each of the `n` nodes starts a comparison that runs for `m` steps.
- Space: O(h), the recursion depth.

### Alternatives

Serializing both trees to strings and checking whether one occurs in the other can reach O(n + m). The serialization needs a marker for missing children and a separator around values, or `12` would match `2`.
