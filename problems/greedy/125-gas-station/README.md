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

- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If the total gas is less than the total cost, can any start work?
2. No, so return `-1`. Otherwise a start exists. If the tank goes negative going from station `a` to `b`, no station between them can be the start.
3. Scan once keeping `tank += gas[i] - cost[i]`. When `tank < 0`, set the candidate start to `i + 1` and reset `tank = 0`. After the scan (and the total check), the candidate is the answer.

</details>
