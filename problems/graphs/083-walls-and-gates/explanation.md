### Approach

Run a breadth-first search from all gates at once. Put every gate (distance 0) in the queue. As the search spreads outward one step at a time, the first time it reaches an empty room is by the shortest path from the nearest gate, so write that distance and queue the room. Walls and already-filled rooms are never entered.

### Complexity

- Time: O(rows * cols), each cell is filled and queued at most once.
- Space: O(rows * cols) for the queue.

### Alternatives

Starting a search from every empty room is far slower, O((rows * cols)^2) in the worst case.
