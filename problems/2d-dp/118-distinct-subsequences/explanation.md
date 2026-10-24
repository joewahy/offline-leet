### Approach

Let `dp[j]` be the number of ways to form the first `j` characters of `t` from the characters of `s` seen so far. For each character of `s`, and for each `j` where `t[j - 1]` equals it, the character can extend a match of the first `j - 1` characters, so add `dp[j - 1]` to `dp[j]`. Going from `j` high to low means each character of `s` is used at most once per update.

### Complexity

- Time: O(m * n).
- Space: O(n), the length of `t`.
