### Approach

Keep four boundaries: top, bottom, left and right. Read the top row left to right, the right column top to bottom, the bottom row right to left, and the left column bottom to top, then shrink all four boundaries by one and repeat.

The two checks (`top < bottom` and `left < right`) stop the last two sides from being read twice when only one row or one column is left.

### Complexity

- Time: O(rows * cols), each cell is read once.
- Space: O(1) extra, not counting the output.
