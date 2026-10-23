# 128. Partition Labels (Medium)

Split the string `s` into as many consecutive parts as possible so that each letter appears in at most one part. Return the lengths of the parts, in order.

## Examples

```
Input:  s = "xyxxyzbzbbisl"
Output: [5, 5, 1, 1, 1]

Input:  s = "abcabc"
Output: [6]
```

## Constraints

- `1 <= len(s) <= 10000`
- `s` consists of lowercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. If a letter appears in a part, that part must reach at least the letter's last occurrence.
2. Record the last index of every letter.
3. Scan the string, keeping `end = max(end, last[c])`. When the index `i` reaches `end`, close the part, record its length, and start the next one.

</details>
