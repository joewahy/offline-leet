### Approach

Put every number in a set so membership checks are O(1). A number starts a sequence only if the number before it is missing (`x - 1 not in s`). From each start, count upward while the next number exists, and keep the longest run.

Starting only at sequence beginnings is what keeps this linear. Without that check, every element would walk its whole run, and a long run would be walked many times over.

### Complexity

- Time: O(n). Each number is visited by the outer loop once, and by the inner loop only as part of the one run it belongs to.
- Space: O(n) for the set.

### Alternatives

Sorting first and scanning for runs is O(n log n).
