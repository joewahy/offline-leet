### Approach

Copy the graph while walking it. Keep a dictionary from each original node to its copy. When you meet a neighbour that has no copy yet, create it and queue it for exploring. For every edge, add the copy of the neighbour to the copy of the current node.

The dictionary doubles as the visited set, which is what stops the walk from looping forever on cycles.

### Complexity

- Time: O(V + E).
- Space: O(V) for the dictionary and the stack.
