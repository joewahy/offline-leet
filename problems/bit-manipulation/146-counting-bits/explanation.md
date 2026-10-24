### Approach

The bits of `i` are the bits of `i >> 1` plus the lowest bit. So the count for `i` is the count for `i >> 1` plus `i & 1`. Fill the answers from 1 up, reusing the earlier ones.

### Complexity

- Time: O(n), one step per number. Counting the bits of each number separately would be O(n log n).
- Space: O(1) extra, not counting the output.
