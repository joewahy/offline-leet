# 76. N-Queens (Hard)

Place `n` queens on an `n x n` chessboard so that no two queens attack each other (no two share a row, a column, or a diagonal).

Return every distinct solution. Each solution is a list of `n` strings, one per row, where `"Q"` is a queen and `"."` is an empty square. The solutions may be returned in any order.

## Examples

```
Input:  n = 4
Output: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]

Input:  n = 1
Output: [["Q"]]
```

## Constraints

- `1 <= n <= 8`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Place queens one row at a time. A row can hold only one queen, so the real choice is the column.
2. A queen at `(r, c)` blocks column `c`, the diagonal `r - c`, and the anti-diagonal `r + c`. Keep a set for each.
3. Recurse row by row, try each column that is not blocked, mark it, recurse, then unmark it. When all `n` rows are filled, build the board strings from the chosen columns.

</details>
