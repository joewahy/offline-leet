### Approach

Each row starts above where the previous one ended, so reading the matrix row by row gives one long sorted list. Binary search that virtual list: for position `mid`, the row is `mid // cols` and the column is `mid % cols`.

### Complexity

- Time: O(log(rows * cols)).
- Space: O(1), nothing is flattened or copied.

### Alternatives

Binary searching for the right row first and then within the row is the same cost. Scanning every cell is O(rows * cols).
