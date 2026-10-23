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

## Hints

- Track three states per day: holding a share, just sold (in cooldown), and resting with nothing.
