# 67. Find Median from Data Stream (Hard)

Design a structure that receives integers one at a time and can report the median of everything received so far. The median is the middle value of the sorted numbers, or the average of the two middle values when the count is even.

Implement `MedianFinder`:

- `MedianFinder()` creates an empty structure.
- `addNum(num)` adds an integer.
- `findMedian()` returns the current median as a float.

`findMedian` is only called after at least one number has been added.

## Examples

```
addNum(1)
findMedian()   -> 1.0
addNum(3)
findMedian()   -> 2.0
addNum(2)
findMedian()   -> 2.0
```

## Constraints

- `-100000 <= num <= 100000`
- At most `10000` calls are made.

## Hints

- Keep the smaller half in a max-heap and the larger half in a min-heap, and keep their sizes within 1 of each other.
