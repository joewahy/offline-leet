### Approach

Comparing each pair of neighbouring words gives at most one rule: the first position where they differ says that one letter comes before another. Collect those rules as edges and put the letters in an order that respects them, which is a topological sort.

Two cases make the input invalid: a word followed by one of its own prefixes (like `abc` then `ab`), and a cycle in the rules. Both return an empty string. Sorting the letters when queueing makes the output deterministic when several orders are valid.

### Complexity

- Time: O(total characters), plus a sort over at most 26 letters.
- Space: O(1), at most 26 letters and their edges.
