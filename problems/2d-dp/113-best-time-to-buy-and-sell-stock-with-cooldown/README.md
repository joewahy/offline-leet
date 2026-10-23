# 113. Best Time to Buy and Sell Stock With Cooldown (Medium)

`prices[i]` is a stock price on day `i`. You may buy and sell as many times as you like, with these rules:

- You can hold at most one share at a time (sell before buying again).
- After you sell, you cannot buy on the very next day (one day of cooldown).

Return the maximum profit.

## Examples

```
Input:  prices = [1, 3, 4, 0, 4]
Output: 6          # buy 1, sell 3, cooldown, buy 0, sell 4

Input:  prices = [1]
Output: 0
```

## Constraints

- `1 <= len(prices) <= 5000`
- `0 <= prices[i] <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Each day you are in one of a few states: holding a share, just sold, or resting. What can you do from each?
2. Track the best profit for each state at the end of each day: `hold`, `sold`, and `rest`.
3. `hold = max(hold, rest - price)`, `sold = old_hold + price`, `rest = max(rest, old_sold)`. Use the old values on the right side of each update. The answer is `max(sold, rest)` after the last day.

</details>
