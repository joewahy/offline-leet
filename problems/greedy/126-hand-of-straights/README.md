# 126. Hand of Straights (Medium)

`hand[i]` is the number written on the `i`-th card. You want to rearrange all the cards into groups of exactly `groupSize` cards, where the numbers in each group are consecutive (like 4, 5, 6).

Return `True` if this is possible, otherwise `False`.

## Examples

```
Input:  hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
Output: True       # [1,2,3], [2,3,4], [6,7,8]

Input:  hand = [1, 2, 3, 4, 5], groupSize = 4
Output: False
```

## Constraints

- `1 <= len(hand) <= 10000`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= len(hand)`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If the number of cards is not a multiple of `groupSize`, it is impossible. Otherwise, which card must start a group?
2. The smallest remaining card must start a group, because nothing smaller could come before it.
3. Count the cards. Go through the values in increasing order: for a value with count `c`, you need `c` copies of each of the next `groupSize - 1` values too. Subtract them, and fail if any is short.

</details>
