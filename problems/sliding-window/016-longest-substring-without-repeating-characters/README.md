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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A repeated letter breaks the substring. What do you need to remember to know whether the next letter is a repeat?
2. Keep a window with a left and a right edge, and a record of the last position of each letter. When the new letter is already inside the window, move the left edge.
3. Store `last[ch] = index`. If `last[ch] >= left`, set `left = last[ch] + 1`. The answer is the largest `right - left + 1` seen, in O(n) time.

</details>
