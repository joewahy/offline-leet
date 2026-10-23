# 2. Valid Anagram (Easy)

Given two strings `s` and `t`, return `True` if `t` is a rearrangement of the letters of `s` (same letters, same counts), otherwise `False`.

## Examples

```
Input:  s = "racecar", t = "carrace"
Output: True

Input:  s = "jar", t = "jam"
Output: False
```

## Constraints

- `1 <= len(s), len(t) <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Hints

- If the lengths differ, you can stop early.
- Compare how many times each character occurs.
