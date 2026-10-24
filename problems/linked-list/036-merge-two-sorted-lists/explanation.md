### Approach

Use a dummy node so you never have to special-case the head. Keep a `tail` pointer. At each step attach whichever of the two current nodes is smaller (the first list wins ties) and advance that list. When one list runs out, attach the rest of the other, which is already sorted.

### Complexity

- Time: O(n + m).
- Space: O(1). The nodes are relinked, not copied.
