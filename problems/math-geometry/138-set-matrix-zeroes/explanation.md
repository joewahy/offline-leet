### Approach

Do it in two phases so zeros you write do not spread. First find every row and column that contains a zero. Then zero out every cell whose row or column is on those lists.

This reference stores the rows and columns in two sets, so it uses O(rows + cols) extra space.

### Complexity

- Time: O(rows * cols).
- Space: O(rows + cols) in this version.

### Alternatives

The O(1) space target uses the first row and the first column of the matrix itself as the markers. You then need two extra flags to remember whether the first row and column held a zero before you started using them as markers.
