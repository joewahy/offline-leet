### Approach

Do it in three steps, all in place.

1. Find the middle with slow and fast pointers, and cut the list there into two halves.
2. Reverse the second half.
3. Weave the two halves together, taking one node from the first half and then one from the reversed second half.

### Complexity

- Time: O(n), a few linear passes.
- Space: O(1).

### Alternatives

Copying the nodes into a list and then relinking by index is simpler but uses O(n) space.
