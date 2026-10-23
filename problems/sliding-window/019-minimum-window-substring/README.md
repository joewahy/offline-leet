# 19. Minimum Window Substring (Hard)

Given strings `s` and `t`, return the shortest substring of `s` that contains every character of `t`, counting repeats (if `t` has two `a`, the window needs two `a`).

If no such substring exists, return `""`. If several windows tie for the shortest length, any one of them is accepted.

## Examples

```
Input:  s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"

Input:  s = "x", t = "xy"
Output: ""
```

## Constraints

- `1 <= len(s), len(t) <= 10000`
- `s` and `t` consist of uppercase and lowercase English letters.

## Hints

- Expand the right edge until the window is valid, then shrink from the left while it stays valid.
