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

## Hints

- Let `dp[i][j]` mean "first `i` letters of `s` match first `j` of `p`". A `*` either matches zero copies (skip two pattern characters) or consumes one more letter.
