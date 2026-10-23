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

## Hints

- Start a depth-first search from each cell that matches the first letter. Mark cells as visited on the way in and unmark them on the way out.
