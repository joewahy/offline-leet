### Approach

Only the `k` largest values matter, and the `k`-th largest of them is the smallest of that group. Keep a min-heap holding the `k` largest values seen. Its root is the answer. When a value arrives, push it, and if the heap has more than `k` entries, pop the smallest. The initial numbers are put through the same trimming.

### Complexity

- Time: O(log k) per `add`.
- Space: O(k).

### Alternatives

Keeping a sorted list of everything and indexing it is O(n log n) per `add` if you re-sort each time.
