### Approach

Choose where the first piece ends. If that piece is a palindrome, keep it and recursively partition the rest of the string. When the start reaches the end of the string, the pieces chosen form a valid partition.

### Complexity

- Time: O(n * 2^n). There can be up to 2^(n-1) ways to cut a string, and checking a piece takes O(n).
- Space: O(n) extra, not counting the output.

### Alternatives

Precomputing which substrings are palindromes with dynamic programming makes each check O(1).
