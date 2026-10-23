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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Compare the last characters of the two strings. What happens if they match? If they do not?
2. Let `dp[i][j]` be the LCS of the first `i` characters of `text1` and the first `j` characters of `text2`.
3. If the characters match, `dp[i][j] = dp[i-1][j-1] + 1`. Otherwise `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`. You only need the previous row.

</details>
