### Approach

Let `dp[i]` be the number of ways to decode the string from position `i` to the end, with `dp[n] = 1` for the empty rest. Work from the right. A `0` cannot start a code, so `dp[i] = 0` there. Otherwise one digit is a valid code, so `dp[i] = dp[i + 1]`. If the next two digits form a number up to 26, they can also be one code, so add `dp[i + 2]`.

### Complexity

- Time: O(n).
- Space: O(n) for the table, or O(1) if you keep only the last two values.

### Watch out

`"06"` is not valid. A leading zero means the digit can neither stand alone nor start a pair.
