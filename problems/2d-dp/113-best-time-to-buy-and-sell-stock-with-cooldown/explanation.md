### Approach

Think of three states at the end of each day: holding a stock, just sold (so on cooldown tomorrow), or resting with no stock and free to buy. Each day, update them from the previous day's states:

- `hold`: keep holding, or buy today from the resting state.
- `sold`: sell today, using what you were holding.
- `rest`: keep resting, or come off cooldown from yesterday's sale.

The answer is the better of `sold` and `rest` at the end, because holding a stock at the end is never best.

### Complexity

- Time: O(n).
- Space: O(1).
