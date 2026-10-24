### Approach

A `*` can act as `(`, `)` or nothing, so instead of trying every choice, track the range of possible counts of unclosed open brackets: `lo` (the fewest possible) and `hi` (the most). A `(` raises both. A `)` lowers both. A `*` could be `)` so it lowers `lo`, or `(` so it raises `hi`.

If `hi` ever drops below 0, there are too many `)` even in the best case, so return false. Clamp `lo` at 0, since a negative count means nothing. At the end, the string is valid if 0 is a possible count, which means `lo == 0`.

### Complexity

- Time: O(n).
- Space: O(1).
