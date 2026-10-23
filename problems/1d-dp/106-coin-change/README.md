# 106. Coin Change (Medium)

`coins` lists the denominations you have (each in unlimited supply) and `amount` is a target sum.

Return the fewest coins that add up to exactly `amount`. If it cannot be made, return `-1`. An amount of `0` needs `0` coins.

## Examples

```
Input:  coins = [1, 5, 10], amount = 12
Output: 3          # 10 + 1 + 1

Input:  coins = [2], amount = 3
Output: -1
```

## Constraints

- `1 <= len(coins) <= 12`
- `1 <= coins[i] <= 10000`, all distinct
- `0 <= amount <= 10000`

## Hints

- `fewest(a) = 1 + min(fewest(a - c))` over the coins `c <= a`. Build the table from `0` upwards.
- A greedy "largest coin first" approach does not always work.
