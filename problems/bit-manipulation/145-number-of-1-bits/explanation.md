### Approach

The expression `n & (n - 1)` clears the lowest set bit of `n`. Repeat it until `n` is 0, counting the steps. The loop runs once per set bit, not once per bit position.

### Complexity

- Time: O(number of set bits), at most 32.
- Space: O(1).
