### Approach

Sort the intervals by start. Then sweep: if the next interval starts at or before the end of the last merged one, they overlap, so extend the last one's end if needed. Otherwise start a new merged interval.

### Complexity

- Time: O(n log n), dominated by the sort.
- Space: O(n) for the output.

### Watch out

Use the larger of the two ends when merging. An interval that sits entirely inside the previous one must not shrink it.
