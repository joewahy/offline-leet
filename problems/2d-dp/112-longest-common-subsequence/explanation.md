### Approach

Let `dp[i][j]` be the longest common subsequence of the first `i` characters of one string and the first `j` of the other. If the last characters match, extend the diagonal result by 1. Otherwise take the better of dropping one character from either string. Each row depends only on the previous one, so two rows are enough.

### Complexity

- Time: O(m * n).
- Space: O(n), the length of one string.
