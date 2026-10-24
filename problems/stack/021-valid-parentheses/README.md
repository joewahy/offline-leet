# 21. Valid Parentheses (Easy)

A string `s` contains only the characters `(`, `)`, `[`, `]`, `{` and `}`. It is valid when every opening bracket is closed by the same kind of bracket, in the right order, and every closing bracket matches an earlier opening one.

Return `True` if `s` is valid, otherwise `False`.

## Examples

```
Input:  s = "[]"
Output: True

Input:  s = "([{}])"
Output: True

Input:  s = "[(])"
Output: False
```

## Constraints

- `1 <= len(s) <= 10^5`

## Hints

- The most recent unmatched opening bracket must be closed first. Which data structure behaves that way?
