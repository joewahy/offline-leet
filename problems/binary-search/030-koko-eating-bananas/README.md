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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If Koko can finish at speed `k`, can she also finish at any faster speed? What does that tell you about the answer?
2. Yes, so feasibility is monotonic: binary search on the speed between 1 and `max(piles)`.
3. To test a speed `k`, add up `ceil(pile / k)` hours over all piles and compare the total with `h`. Use `(pile + k - 1) // k` for the ceiling. Find the smallest speed that works.

</details>
