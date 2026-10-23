# 86. Surrounded Regions (Medium)

`board` is a grid of `"X"` and `"O"`. A region of connected `"O"` cells (connected horizontally or vertically) is surrounded if none of its cells lies on the border of the board. Turn every surrounded region of `"O"` into `"X"`.

Modify `board` in place; return nothing.

## Examples

```
Input:  [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
```

## Constraints

- `1 <= rows, cols <= 60`
- `board[i][j]` is `"X"` or `"O"`.

## Hints

- Instead of finding surrounded regions, find the safe ones: mark every `"O"` reachable from a border `"O"`. Everything else becomes `"X"`.
