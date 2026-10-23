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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You never need to solve the puzzle, only to detect a repeated digit in a row, a column, or a 3x3 box.
2. Keep a set of seen digits for each row, each column, and each box, and check them as you scan each filled cell once.
3. The box for cell `(r, c)` is `(r // 3, c // 3)`. One set of tuples like `('r', r, digit)`, `('c', c, digit)`, `('b', r // 3, c // 3, digit)` covers all three rules.

</details>
