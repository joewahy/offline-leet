# 18. Permutation in String (Medium)

Given two strings `s1` and `s2`, return `True` if some substring of `s2` is a rearrangement of `s1` (same letters, same counts), otherwise `False`.

## Examples

```
Input:  s1 = "abc", s2 = "lecabee"
Output: True       # "cab"

Input:  s1 = "abc", s2 = "lecaabee"
Output: False
```

## Constraints

- `1 <= len(s1), len(s2) <= 10000`
- Both strings consist of lowercase English letters.

## Hints

- Every candidate substring of `s2` has length `len(s1)`. Slide one fixed-size window and update letter counts incrementally.
