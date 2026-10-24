### Approach

An `O` region survives only if it touches the border. So start from the `O` cells on the border and mark everything connected to them as safe. Every other `O` is surrounded and becomes `X`.

Working from the border is simpler than trying to decide for each interior region whether it is enclosed.

### Complexity

- Time: O(rows * cols).
- Space: O(rows * cols) for the safe set and the stack.
