### Approach

Keep a deque of indices whose values are in decreasing order. Before adding index `i`, pop every index at the back whose value is not larger than `nums[i]`, because those can never be a window maximum while `i` is in the window. Drop the front index when it slides out of the window. The front of the deque is always the current maximum.

### Complexity

- Time: O(n). Each index is pushed once and popped at most once.
- Space: O(k), the deque never holds more than one window of indices.

### Alternatives

A max-heap with lazy deletion works in O(n log n). Taking `max` of each window is O(n * k) and times out when `k` is large.
