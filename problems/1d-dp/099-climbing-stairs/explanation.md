### Approach

To reach step `n` you came from step `n - 1` (one step) or step `n - 2` (two steps), so the number of ways is the sum of the previous two. That is the Fibonacci sequence. Only the last two values are needed, so keep two variables instead of a table.

### Complexity

- Time: O(n).
- Space: O(1).
