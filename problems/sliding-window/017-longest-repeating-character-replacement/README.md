# 17. Longest Repeating Character Replacement (Medium)

You are given an uppercase string `s` and an integer `k`. You may change at most `k` characters of `s` into any other uppercase letters.

Return the length of the longest substring that can be made of a single repeated letter using at most `k` changes.

## Examples

```
Input:  s = "XYYX", k = 2
Output: 4          # change the two X into Y

Input:  s = "AAABABB", k = 1
Output: 5
```

## Constraints

- `1 <= len(s) <= 10000`
- `0 <= k <= len(s)`
- `s` consists of uppercase English letters.

## Hints

- A window is fixable when `window length - count of its most common letter <= k`.
