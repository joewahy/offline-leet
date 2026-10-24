### Approach

The same topological sort as Course Schedule, but record the order in which courses are taken. If the order contains every course, return it. If a cycle left some courses stuck, return an empty list.

### Complexity

- Time: O(V + E).
- Space: O(V + E).

### Watch out

Several orders may be valid, and the problem accepts any of them. A checker verifies that every prerequisite comes before the course that needs it.
