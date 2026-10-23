# 103. Longest Palindromic Substring (Medium)

Given a string `s`, return its longest palindromic substring (a contiguous part of `s` that reads the same forwards and backwards). If several have the same maximum length, any one of them is accepted.

## Examples

```
Input:  s = "ababd"
Output: "bab"      # "aba" is also accepted

Input:  s = "abbc"
Output: "bb"
```

## Constraints

- `1 <= len(s) <= 1000`
- `s` consists of digits and English letters.

## Hints

- Every palindrome has a centre (a character or the gap between two). Expand outwards from each centre.
