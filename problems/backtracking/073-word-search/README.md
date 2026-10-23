# 73. Word Search (Medium)

Given a grid of characters `board` and a string `word`, return `True` if `word` can be spelled by walking through horizontally or vertically adjacent cells, starting anywhere. Each cell may be used at most once in a single path.

## Examples

```
Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: True

Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: False
```

## Constraints

- `1 <= rows, cols <= 6`
- `1 <= len(word) <= 15`
- `board` and `word` consist of English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You need to try paths through the grid, undoing a step if it leads nowhere. That is backtracking.
2. Start a depth-first search from every cell that matches the first letter, matching one letter per step in four directions.
3. Mark the current cell as used (for example overwrite it with `#`) before exploring neighbours, and restore it afterwards. Return true when the position reaches `len(word)`, and false when a cell is out of bounds, used, or a mismatch.

</details>
