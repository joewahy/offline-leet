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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Every palindrome has a centre. How many possible centres does a string of length `n` have?
2. Expand outwards from each centre while the two ends match, and remember the longest result.
3. There are `2n - 1` centres: each character, and each gap between two characters (for even lengths). Expansion costs O(n) per centre, so O(n^2) overall.

</details>
