### Approach

Courses and prerequisites form a directed graph. All courses can be taken exactly when the graph has no cycle. Use Kahn's algorithm: count the prerequisites each course still needs (its in-degree), start with the courses that need none, and take them one by one. Finishing a course lowers the count for the courses that follow it, and any that reach zero become available.

If you manage to take every course, there was no cycle.

### Complexity

- Time: O(V + E).
- Space: O(V + E) for the adjacency lists.
