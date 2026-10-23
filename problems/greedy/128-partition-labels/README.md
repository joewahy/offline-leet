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

## Hints

- Record the last position of each letter. Walk through `s`, extending the current part to the farthest last position seen; cut when you reach it.
