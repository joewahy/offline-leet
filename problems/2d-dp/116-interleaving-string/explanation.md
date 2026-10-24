### Approach

Let `dp[i][j]` be true if the first `i + j` characters of `s3` can be built from the first `i` characters of `s1` and the first `j` of `s2`. A cell is true if the last character of `s3` matches the last used character of `s1` and the cell above is true, or it matches the last used character of `s2` and the cell to the left is true. If the lengths do not add up, the answer is false straight away.

The code keeps one row, updating it in place as `i` increases.

### Complexity

- Time: O(m * n).
- Space: O(n), the length of `s2`.
