### Approach

Start with every node in its own group, so there are `n` components. Each edge that joins two different groups merges them and reduces the count by one. An edge between nodes that are already in the same group changes nothing. Union-find with path compression keeps each `find` almost constant time.

### Complexity

- Time: O(V + E), nearly linear.
- Space: O(V).

### Alternatives

Running a DFS or BFS from each unvisited node and counting the searches also gives the answer in O(V + E).
