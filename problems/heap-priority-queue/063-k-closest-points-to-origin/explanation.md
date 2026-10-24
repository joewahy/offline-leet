### Approach

The distance to the origin is monotonic in the squared distance `x * x + y * y`, so compare squared distances and skip the square root. `heapq.nsmallest(k, ...)` keeps only the best `k` candidates while scanning the points.

### Complexity

- Time: O(n log k).
- Space: O(k).

### Alternatives

Sorting all the points is O(n log n), which is also fine here. Quickselect finds the `k` closest in O(n) on average.
