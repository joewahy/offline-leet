### Approach

A board is valid when no digit repeats in any row, column or 3 x 3 box. Scan every cell once and, for each digit, build three keys: its row, its column and its box (`r // 3, c // 3` identifies the box). If any of those keys has been seen, the board is invalid. Otherwise add them to the set.

### Complexity

- Time: O(1). The board is always 9 x 9, so there are 81 cells.
- Space: O(1), at most 243 keys.

### Watch out

Keys include the kind (`"r"`, `"c"`, `"b"`) so that, for example, row 1 and column 1 holding the same digit are not mistaken for a repeat.
