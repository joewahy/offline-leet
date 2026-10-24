### Approach

Let `can[i]` say whether the first `i` characters can be split into dictionary words. `can[0]` is true. For each `i`, look for a start `j` such that `can[j]` is true and `s[j:i]` is a word. Only starts within the longest word's length need checking, which keeps it fast.

### Complexity

- Time: O(n * L), where `L` is the longest word (O(n^2) in the worst case).
- Space: O(n) for the table, plus the word set.

### Alternatives

Recursion with memoization is equivalent. Without memoization it is exponential.
