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

## Hints

- The smallest remaining card must start a group. Take it and the next `groupSize - 1` consecutive values.
- Count cards with a dictionary, and process the values in sorted order.
