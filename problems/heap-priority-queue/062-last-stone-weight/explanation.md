### Approach

Each round needs the two heaviest stones. A heap gives you the maximum quickly. Python only has a min-heap, so store negated weights. Pop two, and if they differ, push back the difference. Stop when at most one stone is left.

### Complexity

- Time: O(n log n). There are at most `n` rounds and each does a few heap operations.
- Space: O(n) for the heap.

### Alternatives

Re-sorting the list after each smash is O(n^2 log n) and times out on large inputs.
