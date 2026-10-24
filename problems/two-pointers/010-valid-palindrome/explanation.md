### Approach

Compare the string from both ends. Keep one pointer at the start and one at the end, skip anything that is not a letter or digit, and compare the two characters ignoring case. If they differ it is not a palindrome. If the pointers meet, it is.

### Complexity

- Time: O(n), each pointer moves inward at most `n` steps in total.
- Space: O(1). Building a cleaned copy of the string and comparing it to its reverse is simpler but uses O(n) space.
