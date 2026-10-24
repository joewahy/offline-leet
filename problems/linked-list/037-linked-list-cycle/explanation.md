### Approach

Use two pointers, one moving a step at a time and one moving two. If the list has a cycle, the fast pointer eventually laps the slow one and they meet on the same node. If there is no cycle, the fast pointer reaches the end first.

### Complexity

- Time: O(n).
- Space: O(1).

### Alternatives

Remembering every visited node in a set also works in O(n) time but uses O(n) space.
