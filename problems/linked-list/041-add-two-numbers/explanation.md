### Approach

Add digit by digit, like on paper. The digits are stored least significant first, so you can start at the heads. At each step add the two digits and the carry, keep `total % 10` as the new digit, and carry `total // 10`. Keep going while either list has digits or a carry is left, so a final carry becomes an extra digit.

### Complexity

- Time: O(max(n, m)).
- Space: O(1) extra, not counting the new list.

### Watch out

A missing digit counts as 0, so lists of different lengths need no special handling.
