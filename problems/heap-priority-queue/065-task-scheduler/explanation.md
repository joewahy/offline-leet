### Approach

Count how often each task appears. The most frequent task sets the schedule: place its copies `n + 1` slots apart, which leaves `top - 1` full frames of length `n + 1`, plus a last partial frame holding one copy of every task tied for the highest count. Everything else fits into the gaps.

So the answer is `(top - 1) * (n + 1) + ties`. If there are so many different tasks that no idle time is ever needed, the answer is just the number of tasks, so take the larger of the two.

### Complexity

- Time: O(n) to count.
- Space: O(1), at most 26 task types.

### Alternatives

Simulating with a max-heap and a cooldown queue is O(n log 26) and gives the actual schedule, which the formula does not.
