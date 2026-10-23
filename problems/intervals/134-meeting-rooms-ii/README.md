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

- `0 <= len(intervals) <= 8000`
- `0 <= start < end <= 10^6`

## Hints

- Sort the start times and the end times separately, then sweep through them, counting how many meetings are running at once.
