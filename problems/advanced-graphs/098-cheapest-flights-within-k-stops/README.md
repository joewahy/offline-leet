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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A plain shortest-path search ignores the limit on stops. What extra information does each state need?
2. Allow at most `k + 1` flights: use Bellman-Ford for `k + 1` rounds, or a heap that tracks the number of stops used.
3. Bellman-Ford: keep a `dist` array. In each of `k + 1` rounds, relax every flight using a copy of the previous round's distances (so one round adds at most one flight). The answer is `dist[dst]`, or `-1` if it is still infinite.

</details>
