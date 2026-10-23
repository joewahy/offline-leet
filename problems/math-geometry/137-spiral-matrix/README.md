# 137. Spiral Matrix (Medium)

Given an `m x n` matrix, return all of its elements in spiral order: start at the top-left, go right along the top row, then down the right column, then left along the bottom row, then up the left column, and keep spiralling inwards.

## Examples

```
Input:  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input:  matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

## Constraints

- `1 <= m, n <= 100`
- `-100 <= matrix[i][j] <= 100`

## Hints

- Keep four boundaries (top, bottom, left, right) and shrink them after walking each side. Watch for a single remaining row or column.
