### Approach

First pass: create a copy of every node and store it in a dictionary keyed by the original node. Second pass: for each original node, set the copy's `next` and `random` by looking up the copies of the originals' `next` and `random`. The `None` key maps to `None`, so null pointers need no special case.

### Complexity

- Time: O(n), two passes.
- Space: O(n) for the dictionary.

### Alternatives

You can get to O(1) extra space by weaving each copy right after its original, setting the random pointers using that layout, and then splitting the two lists apart. It saves memory but is easy to get wrong.
