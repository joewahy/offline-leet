### Approach

Use the same trie as for Implement Trie. To search, follow the word letter by letter. A normal letter goes to one child. A `.` can be any letter, so try every child (not the `$` marker) and succeed if any branch matches the rest of the word.

### Complexity

- Time: O(L) for `addWord`. A search with no dots is O(L), and each dot can branch into up to 26 children, so the worst case is O(26^d * L) for `d` dots.
- Space: O(total characters inserted).
