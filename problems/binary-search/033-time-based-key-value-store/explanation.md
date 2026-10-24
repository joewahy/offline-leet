### Approach

For each key keep two parallel lists: the timestamps and the values. Because `set` is always called with increasing timestamps, the timestamp list stays sorted just by appending. A `get` is then a binary search: `bisect_right` finds the first timestamp greater than the query, and the entry just before it is the latest one that is not later than the query.

### Complexity

- Time: O(1) per `set`, O(log n) per `get`, where `n` is the number of values stored for that key.
- Space: O(n) for everything stored.

### Alternatives

Scanning all timestamps on each `get` is O(n) per call, which times out on large inputs.
