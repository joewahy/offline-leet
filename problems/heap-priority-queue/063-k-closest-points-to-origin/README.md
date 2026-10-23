# 63. K Closest Points to Origin (Medium)

`points[i] = [x, y]` is a point on a 2D plane. Return the `k` points closest to the origin `(0, 0)` by straight-line (Euclidean) distance. The answer may be in any order.

The answer is guaranteed to be unique: there is no tie for the `k`-th closest point.

## Examples

```
Input:  points = [[0, 2], [2, 0], [2, 2]], k = 2
Output: [[0, 2], [2, 0]]

Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
```

## Constraints

- `1 <= k <= len(points) <= 10000`
- `-10000 <= x, y <= 10000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You do not need the actual distances, only their order. Which values compare the same way as distances?
2. Compare squared distances `x*x + y*y` and avoid the square root. Then pick the `k` smallest.
3. Sorting by squared distance is O(n log n). A max-heap of size `k` is O(n log k), and `heapq.nsmallest(k, points, key=...)` does it for you.

</details>
