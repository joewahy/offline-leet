### Approach

The number of rooms needed is the largest number of meetings happening at once. Sort the start times and the end times separately. Walk through the starts: before counting a new meeting, free a room for every meeting that has already ended at or before this start. Then add this meeting and track the peak.

### Complexity

- Time: O(n log n).
- Space: O(n).

### Alternatives

A min-heap of end times (one entry per room in use) gives the same answer.
