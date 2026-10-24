### Approach

Count how often each value occurs, then take the `k` values with the highest counts. `Counter.most_common(k)` does both steps.

### Complexity

- Time: O(n) to count, plus the work to pick the top `k` from the distinct values (at most O(d log k) with a heap, where `d` is the number of distinct values).
- Space: O(n) for the counts.

### Alternatives

Bucket sort reaches true O(n): make a list where index `c` holds the values that occur `c` times, then read it from the highest index down until you have `k` values. A count can never exceed `n`, which is why the buckets are enough.
