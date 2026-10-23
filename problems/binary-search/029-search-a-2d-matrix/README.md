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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Because each row starts after the previous row ends, the whole matrix is in sorted order when read row by row.
2. Treat it as one sorted list of `rows * cols` items and binary search over the indices `0 .. rows * cols - 1`.
3. Convert a flat index `mid` to a cell with `row = mid // cols` and `col = mid % cols`. That gives O(log(m * n)) time.

</details>
