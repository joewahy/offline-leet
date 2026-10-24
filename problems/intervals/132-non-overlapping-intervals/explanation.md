### Approach

To remove the fewest intervals, keep as many non-overlapping ones as possible. Sort by end time and take greedily: an interval that ends earliest leaves the most room for the rest. Keep an interval if it starts at or after the end of the last one kept, otherwise count it as removed.

### Complexity

- Time: O(n log n), from sorting.
- Space: O(1) extra, not counting the sort.

### Alternatives

Sorting by start time and keeping the interval that ends earlier whenever two overlap also works.
