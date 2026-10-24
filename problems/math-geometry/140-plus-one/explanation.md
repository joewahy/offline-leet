### Approach

Add one starting from the last digit. A digit below 9 becomes one more and you are done. A 9 becomes 0 and the carry moves left. If every digit was a 9, the loop ends with all zeros, so put a 1 in front.

### Complexity

- Time: O(n), and usually much less since most numbers stop at the first non-9 digit.
- Space: O(1) extra, not counting the copy of the list.
