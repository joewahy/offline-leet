### Approach

XOR has two useful properties: `x ^ x = 0`, and `x ^ 0 = x`. XOR all the numbers together. Every number that appears twice cancels itself, leaving only the one that appears once. The order does not matter.

### Complexity

- Time: O(n).
- Space: O(1).
