### Approach

Try to start the word at every cell. From a cell, depth-first search into its four neighbours, matching one letter at a time. Mark the cell as used while exploring (here by temporarily writing `#` into it), and restore it on the way back so other paths can use it.

### Complexity

- Time: O(rows * cols * 3^L), where `L` is the word length. Each step has at most three new directions, since you cannot go back.
- Space: O(L), the recursion depth.

### Watch out

If you forget to restore the cell, later searches see a damaged board.
