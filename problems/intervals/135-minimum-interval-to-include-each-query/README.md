# 135. Minimum Interval to Include Each Query (Hard)

`intervals[i] = [left, right]` is a closed interval whose size is `right - left + 1`. For each value in `queries`, find the size of the smallest interval that contains it (`left <= query <= right`). If no interval contains the query, the answer for it is `-1`.

Return the answers in the same order as `queries`.

## Examples

```
Input:  intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,4,6]
Output: [2, 2, 3, 5, 1]

Input:  intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2, -1, 4, 6]
```

## Constraints

- `1 <= len(intervals), len(queries) <= 7000`
- `1 <= left <= right <= 10^6`
- `1 <= queries[j] <= 10^6`

## Hints

- Answer the queries in increasing order. Sweep over the intervals sorted by `left`, pushing each into a min-heap keyed by size, and discard heap tops that end before the query.
