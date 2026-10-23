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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If you zero rows and columns as you scan, the new zeros will cause more zeros. How can you avoid that?
2. First find all the rows and columns that contain a zero, then clear them in a second pass.
3. Use two sets for the row and column indices. For O(1) extra space, store the markers in the first row and first column, remembering separately whether the first row and the first column themselves contained a zero.

</details>
