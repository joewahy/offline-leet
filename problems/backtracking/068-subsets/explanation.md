### Approach

Start with just the empty subset. For each number, every subset built so far can either leave it out (already in the list) or include it, so add a copy of each with the number appended. The list doubles with each number.

### Complexity

- Time: O(n * 2^n), there are 2^n subsets and copying each takes up to `n`.
- Space: O(n) extra, not counting the output.

### Alternatives

A recursive version decides include or exclude for each element in turn. A bitmask from 0 to 2^n - 1 also enumerates all subsets.
