# 104. Palindromic Substrings (Medium)

Return the number of palindromic substrings of `s`. Substrings at different positions count separately, even if they have the same text.

## Examples

```
Input:  s = "abc"
Output: 3          # "a", "b", "c"

Input:  s = "aaa"
Output: 6          # "a" x3, "aa" x2, "aaa"
```

## Constraints

- `1 <= len(s) <= 1000`
- `s` consists of lowercase English letters.

## Hints

- Expand around each of the `2n - 1` possible centres and count every palindrome you pass.
