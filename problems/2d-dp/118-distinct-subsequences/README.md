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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Compare the current letter of `s` with the current letter of `t`. When they are equal, you have two choices.
2. Let `dp[j]` be the number of ways to form the first `j` letters of `t` from the letters of `s` seen so far.
3. For each letter `c` of `s`, going `j` from `len(t)` down to `1`: if `t[j-1] == c`, add `dp[j-1]` to `dp[j]`. Start with `dp[0] = 1`. Going downwards makes sure each letter of `s` is used at most once per step.

</details>
