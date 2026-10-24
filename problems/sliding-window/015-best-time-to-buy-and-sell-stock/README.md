# 15. Best Time to Buy and Sell Stock (Easy)

`prices[i]` is the price of a stock on day `i`. You may buy on one day and sell on a later day, once.

Return the largest profit you can make. If no profit is possible, return `0`.

## Examples

```
Input:  prices = [10, 1, 5, 6, 7, 1]
Output: 6          # buy at 1, sell at 7

Input:  prices = [10, 8, 7, 5, 2]
Output: 0
```

## Constraints

- `1 <= len(prices) <= 10^5`
- `0 <= prices[i] <= 1000`

## Hints

- Track the cheapest price seen so far as you scan.
