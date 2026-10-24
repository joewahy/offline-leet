### Approach

This is a shortest path in a graph where words are nodes and two words are neighbours if they differ by one letter, so use breadth-first search. Comparing every pair of words to find neighbours would be slow. Instead, group words by patterns: replace each letter in turn with `*`, so `hot` becomes `*ot`, `h*t` and `ho*`. Words sharing a pattern are neighbours.

Then search outward from the start word, level by level. The first time you reach the end word, the level is the answer.

### Complexity

- Time: O(N * L^2), building the patterns costs L slices of length L per word, and the search visits each word once.
- Space: O(N * L^2) for the pattern groups.

### Watch out

The end word must be in the list, or the answer is 0.
