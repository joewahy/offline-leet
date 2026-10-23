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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A 90 degree rotation can be done as two simpler operations. Which ones?
2. A clockwise rotation equals a transpose (swap `matrix[i][j]` with `matrix[j][i]`) followed by reversing each row.
3. Transpose by swapping only the pairs with `j > i`, so you do not swap twice, then call `row.reverse()` on every row. Everything happens in place.

</details>
