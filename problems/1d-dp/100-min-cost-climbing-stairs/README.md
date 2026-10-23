# 100. Min Cost Climbing Stairs (Easy)

`cost[i]` is the price you pay to step off stair `i`. After paying you may move up one or two stairs. You may start from stair `0` or stair `1`.

Return the minimum total cost to get to the top, which is one position past the last stair.

## Examples

```
Input:  cost = [1, 2, 3]
Output: 2          # start at index 1, pay 2, jump to the top

Input:  cost = [1, 2, 1, 2, 1, 1, 1]
Output: 4
```

## Constraints

- `2 <= len(cost) <= 1000`
- `0 <= cost[i] <= 999`

## Hints

- The cheapest way to stand on stair `i` is `cost[i-1]` or `cost[i-2]` added to the cheapest way to stand on that earlier stair.
