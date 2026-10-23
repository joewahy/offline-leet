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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The median sits between the smaller half and the larger half of the numbers. You only need the boundary of each half.
2. Keep the smaller half in a max-heap and the larger half in a min-heap, so each heap's top is next to the median.
3. Insert into one heap, then move the top across so every element of the small half is `<=` every element of the large half. Keep the sizes equal or differing by 1. The median is the top of the bigger heap, or the average of both tops. Python's `heapq` is a min-heap, so store negatives for the max-heap.

</details>
