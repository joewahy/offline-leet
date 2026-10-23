# 138. Set Matrix Zeroes (Medium)

`matrix` is an `m x n` grid of integers. If a cell is `0`, set its entire row and its entire column to `0`. Do it in place; the function returns nothing.

## Examples

```
Input:  [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

Input:  [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
```

## Constraints

- `1 <= m, n <= 100`
- `-1000 <= matrix[i][j] <= 1000`

## Hints

- Zeros you create must not cause more zeros. First record which rows and columns to clear, then clear them.
- You can store those markers in the first row and first column to use O(1) extra space.
