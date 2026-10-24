### Approach

Place one queen per row, going down the board. A queen at `(r, c)` conflicts with another when they share a column (`c`), a diagonal going down-right (`r - c` is constant) or a diagonal going down-left (`r + c` is constant). Three sets track which columns and diagonals are taken, so a conflict check is O(1). When all rows are filled, draw the board from the recorded columns.

### Complexity

- Time: O(n!) in the worst case, since each row has fewer free columns than the one above it.
- Space: O(n) extra, not counting the output.
