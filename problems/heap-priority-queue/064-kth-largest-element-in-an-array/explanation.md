### Approach

Keep a min-heap of the `k` largest numbers seen so far. Its root is the `k`-th largest of those. For each remaining number, if it beats the root, replace the root with it. After the scan, the root is the answer.

### Complexity

- Time: O(n log k).
- Space: O(k).

### Alternatives

Sorting the whole array and indexing is O(n log n). Quickselect partitions around a pivot and gets O(n) on average, but O(n^2) in the worst case.
