# 74. Palindrome Partitioning (Medium)

Split the string `s` into consecutive pieces so that every piece is a palindrome. Return every possible way to do this, as a list of lists of pieces. The ways may be returned in any order.

## Examples

```
Input:  s = "aab"
Output: [["a", "a", "b"], ["aa", "b"]]

Input:  s = "a"
Output: [["a"]]
```

## Constraints

- `1 <= len(s) <= 12`
- `s` consists of lowercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Choose where the first piece ends. Which choices are allowed?
2. Only prefixes that are palindromes. For each such prefix, recursively partition the rest of the string.
3. Recurse on a start index: for each `end > start`, if `s[start:end]` is a palindrome, append it, recurse from `end`, then remove it. When `start == len(s)`, record the path. You can precompute a palindrome table to speed up the checks.

</details>
