### Approach

Breadth-first search by minute. Start with all rotten oranges in the queue and count the fresh ones. In each round, every orange in the queue rots its fresh neighbours, which are added for the next round. One round is one minute. Stop when no fresh oranges remain, or when the queue runs dry.

If fresh oranges are still left at the end, they were unreachable, so the answer is -1.

### Complexity

- Time: O(rows * cols).
- Space: O(rows * cols) for the queue.
