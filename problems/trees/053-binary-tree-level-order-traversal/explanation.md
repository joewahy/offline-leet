### Approach

Use a queue. At each round, the queue holds exactly one level of the tree. Take `len(q)` nodes off the front, record their values as one level, and push their children. Repeat until the queue is empty.

### Complexity

- Time: O(n).
- Space: O(w), the queue holds at most one level, and `w` is the widest level (up to about n / 2).
