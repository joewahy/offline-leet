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

## Hints

- You can compare squared distances; no square root is needed.
- A max-heap of size `k` (or `heapq.nsmallest`) avoids sorting everything.
