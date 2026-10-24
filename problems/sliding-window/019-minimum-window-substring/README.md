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

- `1 <= len(s), len(t) <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A window is valid when it contains every needed letter with enough copies. Once a window is valid, can you make it shorter from the left?
2. Expand the right edge until the window is valid, then shrink from the left as long as it stays valid, recording the shortest window.
3. Track how many letters are still missing using a count table. Adding a letter on the right decrements its need. Removing one on the left increments it, and if the need becomes positive the window is invalid again. O(n) overall.

</details>
