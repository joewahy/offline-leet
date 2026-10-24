### Approach

Every palindrome has a centre, either a single character (odd length) or the gap between two characters (even length). There are `2n - 1` centres. For each, expand outward while the two ends match, and remember the longest result.

### Complexity

- Time: O(n^2), each expansion can take up to n steps.
- Space: O(1) apart from the result.

### Alternatives

Manacher's algorithm does it in O(n) but is much harder to write. A DP table of which substrings are palindromes is also O(n^2) time and uses O(n^2) space.
