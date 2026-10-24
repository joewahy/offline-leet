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

- `1 <= len(intervals) <= 10^5`
- `0 <= start <= end <= 10^6`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Overlaps are hard to see when the intervals are in random order. What if they were sorted?
2. Sort by start. Then only the previous merged interval can overlap the next one.
3. Keep a result list. For each interval, if its start is `<=` the last result's end, set that end to the larger of the two ends; otherwise append a new interval.

</details>
