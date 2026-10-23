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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The list is sorted. Relative to the new interval, each interval falls into one of three groups: before it, overlapping it, or after it.
2. Copy the intervals that end before the new one starts, merge all the ones that overlap it, then copy the rest.
3. While `intervals[i][1] < new[0]`, copy. While `intervals[i][0] <= new[1]`, set `new = [min of starts, max of ends]`. Append the merged interval, then copy the remaining intervals.

</details>
