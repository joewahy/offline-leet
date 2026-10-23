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

## Hints

- Try every prefix that is a palindrome, then partition the remainder recursively.
