# 129. Valid Parenthesis String (Medium)

The string `s` contains only `(`, `)` and `*`. The `*` is a wildcard: it may be treated as `(`, as `)`, or as an empty string.

Return `True` if `s` can be made a valid parentheses string, otherwise `False`. A valid string has every `(` matched by a later `)` and every `)` matched by an earlier `(`.

## Examples

```
Input:  s = "((**))"
Output: True

Input:  s = "(((*)"
Output: False
```

## Constraints

- `1 <= len(s) <= 100`
- Each character is `(`, `)` or `*`.

## Hints

- Track the smallest and largest possible number of unmatched `(` as you scan. If the largest goes negative, you have too many `)`; at the end the smallest must be able to reach 0.
