# 116. Interleaving String (Medium)

Given strings `s1`, `s2` and `s3`, return `True` if `s3` can be formed by interleaving `s1` and `s2`: split each of them into pieces, then alternate pieces from `s1` and `s2` while keeping the order of letters inside each string.

Put simply, you read through `s3` and, at each letter, take it from the front of what remains of `s1` or of `s2`.

## Examples

```
Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: True

Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: False
```

## Constraints

- `0 <= len(s1), len(s2) <= 100`, and `0 <= len(s3) <= 200`
- All strings consist of lowercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If the lengths of `s1` and `s2` do not add up to `len(s3)`, you can stop right away. Otherwise, each next character of `s3` has to come from one of the two strings.
2. Let `dp[i][j]` be whether the first `i` letters of `s1` and the first `j` letters of `s2` can form the first `i + j` letters of `s3`.
3. `dp[i][j]` is true if `dp[i-1][j]` is true and `s1[i-1] == s3[i+j-1]`, or `dp[i][j-1]` is true and `s2[j-1] == s3[i+j-1]`. `dp[0][0]` is true. One row is enough.

</details>
