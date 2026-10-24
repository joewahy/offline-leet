### Approach

Let `dp[a]` be the fewest coins that make amount `a`, with `dp[0] = 0`. For each amount, try every coin that fits: the best way to make `a` using coin `c` is one coin plus the best way to make `a - c`. Take the minimum. If an amount stays at infinity, it cannot be made, so return -1.

### Complexity

- Time: O(amount * coins).
- Space: O(amount).

### Alternatives

A greedy choice of the biggest coin first fails for coin sets like `[1, 3, 4]` and amount 6, where 3 + 3 beats 4 + 1 + 1.
