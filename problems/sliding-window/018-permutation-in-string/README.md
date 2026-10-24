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

- `1 <= len(s1), len(s2) <= 10^5`
- Both strings consist of lowercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A permutation of `s1` has exactly the same letter counts as `s1`. What window length are you looking for in `s2`?
2. Slide a window of length `len(s1)` across `s2` and compare its letter counts with the counts of `s1`.
3. Update the counts incrementally: add the letter entering on the right, remove the one leaving on the left. Comparing two 26-entry count tables is O(26), so the whole scan is O(n).

</details>
