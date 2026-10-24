### Approach

A permutation of `s1` is any substring of `s2` of the same length with the same letter counts. Slide a window of length `len(s1)` across `s2`, updating its letter counts as it moves: add the new character on the right, remove the old one on the left. Check after each move whether the counts equal `s1`'s.

Counts that fall to zero are deleted so the two `Counter` objects compare equal.

### Complexity

- Time: O(n). Each step updates two counts, and comparing counters looks at at most 26 letters.
- Space: O(1), at most 26 letters in each counter.

### Alternatives

Sorting every window and comparing is O(n * m log m) and too slow when `s1` is large.
