### Approach

The water held between two lines is the distance between them times the shorter height. Start with the widest pair, at both ends. To find anything better, you must move the shorter line, because moving the taller one only reduces the width without being able to raise the limiting height. So move the shorter side inward and keep the best area seen.

### Complexity

- Time: O(n), one inward sweep.
- Space: O(1).

### Alternatives

Trying every pair is O(n^2) and times out on large inputs.
