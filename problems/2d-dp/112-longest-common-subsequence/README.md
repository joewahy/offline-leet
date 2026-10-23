# 112. Longest Common Subsequence (Medium)

Return the length of the longest common subsequence of two strings `text1` and `text2`. A subsequence keeps the original order of characters but may skip some. If the strings share nothing, return `0`.

## Examples

```
Input:  text1 = "cat", text2 = "crabt"
Output: 3          # "cat"

Input:  text1 = "abc", text2 = "def"
Output: 0
```

## Constraints

- `1 <= len(text1), len(text2) <= 1000`
- Both strings consist of lowercase English letters.

## Hints

- `dp[i][j]` is the answer for the first `i` letters of `text1` and the first `j` of `text2`. If the last letters match, add 1 to `dp[i-1][j-1]`; otherwise take the better of dropping one letter.
