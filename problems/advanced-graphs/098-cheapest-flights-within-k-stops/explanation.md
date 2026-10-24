### Approach

A cheaper path may use more stops than the problem allows, so plain Dijkstra on cities is not enough. Track the number of flights used as part of the state, `(city, flights used)`, and run Dijkstra over those states using a heap ordered by cost. Skip a state if you reached it before at the same or lower cost. Stop expanding when the stop limit is exceeded.

The first time the heap produces the destination, that cost is the cheapest valid one.

### Complexity

- Time: O(k * E) in the worst case, since each edge is relaxed at most once per level of stops.
- Space: O(V) or more for the state table (up to V * k entries).

### Alternatives

Bellman-Ford limited to `k + 1` rounds is shorter and has the same O(k * E) bound.
