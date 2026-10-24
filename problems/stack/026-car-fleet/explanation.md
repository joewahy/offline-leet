### Approach

Sort the cars by position, starting from the car closest to the target. For each car compute the time it would take to arrive alone. If it takes longer than the slowest fleet ahead of it, it can never catch that fleet, so it starts a new fleet. If it takes the same or less, it catches up and merges into the fleet ahead, which sets the pace.

### Complexity

- Time: O(n log n), dominated by sorting.
- Space: O(n) for the sorted list.

### Watch out

A car that reaches the same moment as the fleet ahead joins it, so the comparison is strictly greater.
