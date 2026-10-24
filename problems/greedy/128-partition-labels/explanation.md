### Approach

Record the last index at which each letter appears. Then sweep the string with a window end: for each position, extend the end to the last occurrence of that letter. When the sweep reaches the end of the window, every letter inside it has all its occurrences inside it, so you can cut here. Record the length and start the next part.

### Complexity

- Time: O(n).
- Space: O(1), at most 26 letters.
