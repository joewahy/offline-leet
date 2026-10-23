# 131. Merge Intervals (Medium)

Given a list of intervals `[start, end]` in any order, merge all intervals that overlap (intervals that only touch at an endpoint, like `[1, 2]` and `[2, 3]`, also merge) and return the merged intervals sorted by `start`.

## Examples

```
Input:  intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]

Input:  intervals = [[1,2],[2,3]]
Output: [[1,3]]
```

## Constraints

- `1 <= len(intervals) <= 10000`
- `0 <= start <= end <= 10^6`

## Hints

- Sort by start. Then each interval either extends the last merged one or begins a new one.
