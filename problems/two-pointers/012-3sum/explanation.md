### Approach

Sort the list. Fix the first number `a`, then find two more numbers that sum to `-a` with two pointers on the rest of the list, the same way as in Two Sum II.

Duplicates are skipped at two places, so no triple is reported twice: when the first number repeats the one before it, and after a triple is found, the left pointer moves past equal values. Once `a` is positive, no later triple can sum to zero, so the loop stops.

### Complexity

- Time: O(n^2). Sorting is O(n log n), and each fixed number costs one linear two-pointer sweep.
- Space: O(1) extra, not counting the sort or the output.

### Watch out

The answer must contain no duplicate triples, and checking each triple against a set of found ones is slower and more awkward than skipping equal neighbours in a sorted list.
