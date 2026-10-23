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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A region is safe if it touches the border. Which `O` cells can you identify right away?
2. Start from the border cells that are `O` and mark every `O` connected to them as safe.
3. After marking, every `O` that is not safe is surrounded, so turn it into `X`. Leave the safe ones as `O`.

</details>
