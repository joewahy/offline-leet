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

- `1 <= len(s) <= 10^5`
- `0 <= k <= len(s)`
- `s` consists of uppercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. For a window, how many replacements are needed to make all its letters the same?
2. Replacements needed = window length minus the count of its most frequent letter. The window is valid while that is at most `k`.
3. Grow the right edge while counting letters. When `length - max_count > k`, move the left edge by one. The answer is the longest valid window, in O(n) time (there are only 26 letters, so finding the max count is cheap).

</details>
