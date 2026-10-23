# 98. Cheapest Flights Within K Stops (Medium)

There are `n` cities labelled `0` to `n - 1`. `flights[i] = [from, to, price]` is a one-way flight.

Return the cheapest price to travel from city `src` to city `dst` using at most `k` stops (cities visited in between, so at most `k + 1` flights). If there is no such route, return `-1`.

## Examples

```
Input:  n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700

Input:  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
```

## Constraints

- `1 <= n <= 500`
- `0 <= len(flights) <= 3000`
- `0 <= src, dst, k < n`, and `src != dst`
- `1 <= price <= 300`; there is at most one flight per ordered pair of cities.

## Hints

- A plain Dijkstra can pick a cheap path that uses too many stops. Track the number of stops in the state, or run Bellman-Ford for exactly `k + 1` rounds.
