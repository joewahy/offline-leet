### Approach

The same centre expansion as Longest Palindromic Substring, but instead of keeping the longest, count one palindrome every time the expansion succeeds. Each successful step outward is one more palindromic substring with that centre.

### Complexity

- Time: O(n^2).
- Space: O(1).
