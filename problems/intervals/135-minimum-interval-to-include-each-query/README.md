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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Checking every interval for every query is too slow. What if you handled the queries in sorted order?
2. Sort the intervals by start and the queries in ascending order, and sweep through them together.
3. For each query, push into a min-heap `(size, end)` every interval whose start is `<= query`. Pop the top while its end is `< query`. The top's size is the answer, or `-1` if the heap is empty. Remember the original order of the queries.

</details>
