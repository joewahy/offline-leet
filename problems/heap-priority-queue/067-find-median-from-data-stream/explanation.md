### Approach

Split the numbers into a smaller half and a larger half. Keep the smaller half in a max-heap (as negated values) and the larger half in a min-heap, so the middle is always at the two roots. The halves are kept balanced, with the smaller half equal in size or one bigger.

On each insert, push the number through the small heap and move its largest element across to the large heap, then move one back if the large heap ended up bigger. The median is the root of the small heap, or the average of the two roots when the count is even.

### Complexity

- Time: O(log n) per `addNum`, O(1) per `findMedian`.
- Space: O(n).

### Alternatives

Sorting on every query is O(n log n) each time. Inserting into a sorted list with `bisect` is O(n) per insert because of the shifting.
