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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Taking the biggest coin each time can give the wrong answer. Think about the fewest coins for every smaller amount.
2. Let `dp[a]` be the fewest coins for amount `a`. To make `a`, the last coin is some `c`, so look at `dp[a - c]`.
3. `dp[0] = 0` and `dp[a] = 1 + min(dp[a - c])` over coins `c <= a` (use infinity when impossible). Fill from 1 up to `amount`, and return `-1` if `dp[amount]` is still infinity.

</details>
