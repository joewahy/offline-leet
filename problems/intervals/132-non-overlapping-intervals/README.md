# 132. Non-overlapping Intervals (Medium)

Given a list of intervals `[start, end]`, return the minimum number of intervals you must remove so that the remaining ones do not overlap. Intervals that only touch at an endpoint (like `[1, 2]` and `[2, 3]`) do not overlap.

## Examples

```
Input:  intervals = [[1,2],[2,4],[1,4]]
Output: 1          # remove [1,4]

Input:  intervals = [[1,2],[1,2],[1,2]]
Output: 2
```

## Constraints

- `1 <= len(intervals) <= 10000`
- `0 <= start < end <= 10^6`

## Hints

- Greedy: sort by end. Keep an interval if it starts at or after the end of the last kept one; otherwise remove it.
