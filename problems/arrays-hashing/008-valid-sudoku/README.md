# 8. Valid Sudoku (Medium)

You are given a 9 x 9 Sudoku board as a list of lists of single-character strings. Empty cells are `"."`.

Return `True` if the filled cells do not break any Sudoku rule, otherwise `False`. A board is valid when:

- each row has no repeated digit,
- each column has no repeated digit,
- each of the nine 3 x 3 boxes has no repeated digit.

You only check the filled cells. The board does not have to be solvable.

## Examples

```
A board with 5 at (0,0) and another 5 later in the same row  ->  False
A board with only 5 at (0,0) and 3 at (0,1)                  ->  True
```

## Constraints

- `len(board) == 9` and `len(board[i]) == 9`
- Each cell is `"1"` to `"9"` or `"."`.

## Hints

- Keep one set per row, per column, and per box.
- The box for cell `(r, c)` is `(r // 3, c // 3)`.
