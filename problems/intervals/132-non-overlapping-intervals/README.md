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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. When two intervals overlap, you must remove one. Which one is the better choice to keep?
2. Keep the one that ends earlier, since it leaves the most room for the rest.
3. Sort by end time. Track the end of the last kept interval. For each interval, if its start is `>=` that end, keep it; otherwise count one removal.

</details>
