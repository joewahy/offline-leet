# 95. Network Delay Time (Medium)

A network has `n` nodes labelled `1` to `n`. `times[i] = [u, v, w]` means a signal sent from node `u` reaches node `v` after `w` time units (a directed connection).

A signal is sent from node `k`. Return the minimum time until all nodes have received it, or `-1` if some node can never receive it.

## Examples

```
Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Input:  times = [[1,2,1]], n = 2, k = 2
Output: -1
```

## Constraints

- `1 <= k <= n <= 1000`
- `0 <= len(times) <= 5000`
- `1 <= w <= 100`, and each `(u, v)` pair appears at most once

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The signal takes the fastest route to each node. Which algorithm finds shortest paths with positive weights?
2. Dijkstra's algorithm from node `k`, using a min-heap.
3. Pop the smallest `(time, node)`, skip it if the node is already finalized, record its time, and push its neighbours with `time + w`. The answer is the largest finalized time, or `-1` if fewer than `n` nodes were reached.

</details>
