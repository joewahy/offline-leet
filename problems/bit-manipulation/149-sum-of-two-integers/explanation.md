### Approach

Add using only bit operations, like a hand-written carry. `a ^ b` is the sum without carries, and `(a & b) << 1` is the carry. Repeat with those two values until there is no carry left.

Python integers have no fixed size, so negative numbers would keep a carry going forever. The code limits every value to 32 bits with a mask, and at the end converts a value above the largest positive 32-bit number back into a negative Python integer.

### Complexity

- Time: O(1), at most 32 rounds.
- Space: O(1).
