# 118. Distinct Subsequences (Hard)

Given strings `s` and `t`, return the number of distinct subsequences of `s` that are equal to `t`. Subsequences made from different positions of `s` count separately, even if the text is the same.

## Examples

```
Input:  s = "caat", t = "cat"
Output: 2          # use either 'a'

Input:  s = "babgbag", t = "bag"
Output: 5
```

## Constraints

- `1 <= len(s) <= 1000`, `1 <= len(t) <= 1000`
- Both strings consist of English letters.
- The tests are chosen so the answer fits in a 32-bit integer.

## Hints

- `dp[i][j]` is the number of ways the first `j` letters of `t` appear in the first `i` letters of `s`. If `s[i-1] == t[j-1]` you may use that letter or skip it.
