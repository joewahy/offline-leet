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

## Hints

- Place one queen per row. Track which columns and diagonals (`row - col` and `row + col`) are taken.
