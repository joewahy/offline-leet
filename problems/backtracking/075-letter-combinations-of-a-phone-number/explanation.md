### Approach

Build the combinations one digit at a time. Start with the empty string. For each digit, replace every string built so far with one copy for each letter that digit can stand for. After the last digit, you have all combinations.

### Complexity

- Time: O(4^n * n), at most 4 letters per digit.
- Space: O(n) extra, not counting the output.

### Watch out

An empty input returns an empty list, not a list with one empty string.
