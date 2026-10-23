# 114. Coin Change II (Medium)

`coins` lists coin denominations (each in unlimited supply) and `amount` is a target sum.

Return the number of different combinations of coins that add up to exactly `amount`. Orders do not matter (`1 + 2` and `2 + 1` are the same combination). If no combination works, return `0`. An amount of `0` has exactly one combination: using no coins.

## Examples

```
Input:  amount = 4, coins = [1, 2, 3]
Output: 4          # 1+1+1+1, 1+1+2, 2+2, 1+3

Input:  amount = 3, coins = [2]
Output: 0
```

## Constraints

- `1 <= len(coins) <= 100`
- `1 <= coins[i] <= 1000`, all distinct
- `0 <= amount <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Counting combinations differs from counting sequences: `1 + 2` and `2 + 1` are the same combination.
2. Process one coin type at a time, so each combination is counted once, in a fixed order of coins.
3. Let `ways[a]` be the number of combinations for amount `a`, with `ways[0] = 1`. For each coin `c`, loop `a` from `c` up to `amount` and do `ways[a] += ways[a - c]`. The loop over coins must be the outer one.

</details>
