# 121. Regular Expression Matching (Hard)

Implement matching of the string `s` against the pattern `p`, where the pattern supports two special characters:

- `.` matches any single character.
- `*` matches zero or more copies of the character just before it.

The pattern must match the entire string `s`, not just part of it. Return `True` if it does, otherwise `False`.

## Examples

```
Input:  s = "aa", p = "a*"
Output: True

Input:  s = "ab", p = ".*"
Output: True

Input:  s = "mississippi", p = "mis*is*p*."
Output: False
```

## Constraints

- `0 <= len(s) <= 30`, `0 <= len(p) <= 30`
- `s` contains only lowercase letters. `p` contains lowercase letters, `.` and `*`.
- Every `*` follows a letter or a `.`, so patterns like `*a` or `a**` do not occur.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Compare characters from the front or the back. What special cases does `*` create?
2. Let `dp[i][j]` be whether the first `i` letters of `s` match the first `j` characters of `p`. Handle a normal character or `.` first.
3. For a plain character or `.`, `dp[i][j] = dp[i-1][j-1]` if they match. For `x*`, either use it zero times (`dp[i][j-2]`) or, if `x` matches `s[i-1]`, use one more copy (`dp[i-1][j]`). Patterns like `a*b*` can match the empty string, so initialise the first row.

</details>
