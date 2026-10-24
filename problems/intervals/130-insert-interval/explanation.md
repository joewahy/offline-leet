### Approach

The intervals are sorted and do not overlap, so the new one splits them into three groups. Copy over everything that ends before the new interval starts. Then merge every interval that overlaps it, by widening the new interval to the smallest start and largest end. Finally copy over the rest, which all start after it ends.

### Complexity

- Time: O(n), one pass.
- Space: O(n) for the output.

### Alternatives

Appending the new interval and running Merge Intervals works but costs O(n log n) for the sort.
