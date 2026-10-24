### Approach

Think of the jumps as a breadth-first search over ranges. `end` is the farthest index reachable with the jumps used so far, and `far` is the farthest reachable with one more jump from anywhere in the current range. When you arrive at `end`, you must take another jump, so increase the count and extend `end` to `far`.

The loop stops one short of the last index, so you do not count an extra jump when you are already there.

### Complexity

- Time: O(n).
- Space: O(1).
