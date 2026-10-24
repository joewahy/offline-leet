### Approach

Let `ways[a]` be the number of ways to make amount `a`. Process the coins one at a time, and for each coin go upward through the amounts, adding `ways[a - c]` to `ways[a]`. Looping over coins on the outside means each combination is counted once, in a fixed coin order, instead of once per ordering.

### Complexity

- Time: O(amount * coins).
- Space: O(amount).

### Watch out

Swapping the loops (amounts outside, coins inside) counts ordered sequences, so `1 + 2` and `2 + 1` become different ways. That is a different problem.
