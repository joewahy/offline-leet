# 125. Gas Station (Medium)

There are `n` gas stations on a circular road. Station `i` has `gas[i]` units of fuel, and driving from station `i` to the next one (station `i + 1`, wrapping around) costs `cost[i]` units. Your tank starts empty and is unlimited in size.

Return the index of a station where you can start and drive once around the circle clockwise. If it is impossible, return `-1`. If there is a solution, it is unique.

## Examples

```
Input:  gas = [1, 2, 3, 4], cost = [2, 2, 4, 1]
Output: 3

Input:  gas = [1, 2, 3], cost = [2, 3, 2]
Output: -1
```

## Constraints

- `1 <= n <= 10000`
- `0 <= gas[i], cost[i] <= 1000`

## Hints

- If the total gas is less than the total cost, no start works.
- If you run out of fuel going from `i` to `j`, no station in between can be the start; try `j + 1`.
