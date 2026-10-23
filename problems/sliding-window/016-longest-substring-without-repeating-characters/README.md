# 16. Longest Substring Without Repeating Characters (Medium)

Given a string `s`, return the length of the longest contiguous substring in which no character appears more than once.

## Examples

```
Input:  s = "zxyzxyz"
Output: 3          # "zxy"

Input:  s = "xxxx"
Output: 1
```

## Constraints

- `0 <= len(s) <= 10000`
- `s` contains printable ASCII characters (letters, digits, symbols, spaces).

## Hints

- Keep a window `[left, right]`. When a repeat appears, move `left` just past the earlier copy.
