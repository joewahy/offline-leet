### Approach

Build each string one character at a time. You may add an opening bracket while fewer than `n` have been used. You may add a closing bracket only when it would close one that is open, which means more openers than closers so far. Every string that reaches length `2n` is valid, and no invalid prefix is ever explored.

### Complexity

- Time: O(4^n / sqrt(n)), the number of valid strings (the Catalan number), each costing a little to build.
- Space: O(n) for the recursion, not counting the output.

### Alternatives

Generating every string of brackets and filtering the valid ones does O(2^(2n)) work, which is far more.
