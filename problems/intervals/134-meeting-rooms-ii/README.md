# 134. Meeting Rooms II (Medium)

You are given a list of meeting time intervals, each an `Interval` object with `start` and `end` attributes (the meeting occupies `[start, end)`). Return the minimum number of rooms needed so that all meetings can take place. A meeting that starts exactly when another ends can reuse its room.

In the tests an interval is written as `[start, end]`.

## Examples

```
Input:  intervals = [[0,40],[5,10],[15,20]]
Output: 2

Input:  intervals = [[4,9]]
Output: 1
```

## Constraints

- `0 <= len(intervals) <= 10^5`
- `0 <= start < end <= 10^6`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The number of rooms needed is the largest number of meetings running at the same moment.
2. Look at the start and end events in time order. A start adds a meeting, an end removes one.
3. Sort the start times and the end times separately. Sweep through the starts: while the earliest end is `<=` the current start, free a room. Then use a room. Track the maximum in use. A min-heap of end times also works.

</details>
