### Approach

For each bar, the best rectangle using it as the shortest bar extends left and right until a shorter bar appears. A stack of `(start index, height)` pairs in increasing height order finds those limits in one pass.

When a bar is shorter than the one on top, the top bar cannot extend any further right. Pop it and compute its area from its start index to the current index. The new bar then inherits that start index, since it can extend as far left as the popped bar could. A zero-height bar is appended to the input so everything left on the stack is popped at the end.

### Complexity

- Time: O(n). Each bar is pushed and popped once.
- Space: O(n).

### Alternatives

Expanding left and right from every bar is O(n^2) and times out on flat or sorted histograms.
