# 136. Rotate Image (Medium)

`matrix` is an `n x n` grid of integers. Rotate it 90 degrees clockwise, in place: modify the given matrix directly and do not allocate another matrix. The function returns nothing.

## Examples

```
Input:  [[1, 2], [3, 4]]
Output: [[3, 1], [4, 2]]

Input:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Constraints

- `1 <= n <= 100`
- `-1000 <= matrix[i][j] <= 1000`

## Hints

- Transposing the matrix and then reversing each row gives a clockwise rotation.
- Or rotate four cells at a time, layer by layer.
