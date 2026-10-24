### Approach

A 90-degree clockwise rotation is the same as flipping the matrix over its main diagonal (transpose) and then reversing every row. Both steps work in place, so no second matrix is needed.

### Complexity

- Time: O(n^2), every cell is touched a constant number of times.
- Space: O(1).
