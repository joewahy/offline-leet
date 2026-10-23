# 29. Search a 2D Matrix (Medium)

`matrix` is a grid of integers where every row is sorted in ascending order, and the first number of each row is larger than the last number of the row above.

Return `True` if `target` appears in the matrix, otherwise `False`. Aim for O(log(m * n)) time.

## Examples

```
Input:  matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target = 10
Output: True

Input:  matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target = 15
Output: False
```

## Constraints

- `1 <= rows, cols <= 100`
- `-10000 <= matrix[i][j], target <= 10000`

## Hints

- Read the grid as one long sorted list. Index `k` maps to row `k // cols`, column `k % cols`.
