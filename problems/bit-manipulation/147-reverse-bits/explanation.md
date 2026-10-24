### Approach

Build the result bit by bit. Repeat 32 times: shift the result left by one, copy the lowest bit of `n` into it, and shift `n` right. After 32 rounds the first bit read has ended up as the highest bit of the result.

### Complexity

- Time: O(1), always 32 steps.
- Space: O(1).
