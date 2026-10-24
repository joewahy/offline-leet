### Approach

Walk the houses left to right and track two numbers: the best total if the current house is skipped, and the best if it is robbed. Robbing a house means the previous one was skipped, so `take = previous skip + this house`. Skipping means you keep the better of the two earlier results. The answer is the better of the two at the end.

### Complexity

- Time: O(n).
- Space: O(1).
