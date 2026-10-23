# 26. Car Fleet (Medium)

Several cars drive along a one-lane road toward a destination `target` miles away. Car `i` starts at `position[i]` and drives at a constant `speed[i]` miles per hour.

A car can never overtake the car in front of it. If it catches up, it slows down and travels at the same speed right behind it. A group of cars that end up driving together is a fleet, and a lone car is also a fleet. A car that catches another exactly at the destination counts as part of that fleet.

Return the number of fleets that arrive at the destination.

## Examples

```
Input:  target = 10, position = [1, 4], speed = [3, 2]
Output: 1

Input:  target = 10, position = [4, 1, 0, 7], speed = [2, 2, 1, 1]
Output: 3
```

## Constraints

- `1 <= len(position) == len(speed) <= 10000`
- `0 <= position[i] < target <= 10^6`, all positions are distinct
- `1 <= speed[i] <= 100`

## Hints

- Sort by starting position, closest to the destination first. Compute how long each car needs to arrive on its own.
- A car joins the fleet ahead if its own time is not longer than that fleet's time.
