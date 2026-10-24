### Approach

Let `dp[i][j]` be true if the first `i` characters of `s` match the first `j` of the pattern. A normal character or `.` needs the previous characters to match and the current ones to be equal (or the pattern to be `.`). For a `*`, there are two choices: use it zero times (look at `dp[i][j - 2]`), or use it once more when the character before the star matches the current character (look at `dp[i - 1][j]`).

The first row handles patterns like `a*b*` that can match an empty string.

### Complexity

- Time: O(m * n).
- Space: O(m * n).
