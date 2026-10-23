# 133. Meeting Rooms (Easy)

You are given a list of meeting time intervals, each an `Interval` object with `start` and `end` attributes (the meeting occupies `[start, end)`). Return `True` if one person can attend all the meetings, i.e. no two meetings overlap. A meeting that starts exactly when another ends does not overlap it.

In the tests an interval is written as `[start, end]`.

## Examples

```
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: False

Input:  intervals = [[5,8],[9,15]]
Output: True
```

## Constraints

- `0 <= len(intervals) <= 8000`
- `0 <= start < end <= 10^6`

## Hints

- Sort by start time, then compare each meeting with the one before it.
