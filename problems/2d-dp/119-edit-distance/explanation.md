### Approach

Let `dp[i][j]` be the fewest edits to turn the first `i` characters of `word1` into the first `j` of `word2`. If the last characters are equal, no edit is needed there, so take the diagonal. Otherwise take 1 plus the best of three edits: replace (diagonal), delete (the cell above), or insert (the cell to the left). The first row and column are just the lengths. Only the previous row is needed.

### Complexity

- Time: O(m * n).
- Space: O(n).
