### Approach

Keep a stack of indices of days that are still waiting for a warmer day. When a new day is warmer than the day on top of the stack, that waiting day has found its answer, which is the difference in indices. Pop it and repeat. Then push the current day.

The temperatures on the stack are always in non-increasing order, so each warmer day resolves exactly the colder days it should.

### Complexity

- Time: O(n). Each index is pushed once and popped at most once.
- Space: O(n).

### Alternatives

Scanning forward from every day is O(n^2) on inputs where the temperature never rises.
