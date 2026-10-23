# 130. Insert Interval (Medium)

`intervals` is a list of non-overlapping intervals `[start, end]`, sorted by `start`. Insert `newInterval` into it so the list stays sorted and has no overlaps, merging any intervals that overlap (intervals that only touch at an endpoint, like `[1, 2]` and `[2, 3]`, also merge).

Return the resulting list of intervals.

## Examples

```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Constraints

- `0 <= len(intervals) <= 10000`
- `0 <= start <= end <= 10^5`
- `intervals` is sorted by `start` and has no overlaps.

## Hints

- Copy the intervals that end before the new one starts, merge everything that overlaps it, then copy the rest.
