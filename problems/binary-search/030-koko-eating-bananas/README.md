# 30. Koko Eating Bananas (Medium)

There are several piles of bananas; `piles[i]` is the size of pile `i`. You have `h` hours. Each hour you choose one pile and eat up to `k` bananas from it. If the pile has fewer than `k` bananas you eat them all and waste the rest of the hour.

Return the smallest integer eating speed `k` that lets you finish every pile within `h` hours.

## Examples

```
Input:  piles = [1, 4, 3, 2], h = 9
Output: 2

Input:  piles = [25, 10, 23, 4], h = 4
Output: 25
```

## Constraints

- `1 <= len(piles) <= 10000`
- `len(piles) <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Hints

- If speed `k` works, so does any larger speed. That means you can binary search on `k`, between 1 and the biggest pile.
- Hours needed at speed `k` is the sum of `ceil(pile / k)`.
