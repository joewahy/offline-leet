### Approach

Two strings are anagrams exactly when every letter appears the same number of times in both. `Counter` builds that tally for each string, and comparing the two tallies answers the question.

### Complexity

- Time: O(n) to count both strings.
- Space: O(1), because the alphabet is fixed at 26 letters, so each tally holds at most 26 entries.

### Alternatives

Comparing `sorted(s)` with `sorted(t)` is shorter but costs O(n log n).
