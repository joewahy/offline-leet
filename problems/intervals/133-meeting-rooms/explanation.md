### Approach

Sort the meetings by start time. One person can attend all of them exactly when each meeting ends no later than the next one starts. If any meeting overlaps the one after it, the answer is false. Touching at a single moment is fine.

### Complexity

- Time: O(n log n).
- Space: O(n) for the sorted copy.

### Alternatives

Comparing every pair is O(n^2).
