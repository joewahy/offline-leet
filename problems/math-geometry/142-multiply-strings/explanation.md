### Approach

Multiply the way you do on paper. The product of a digit in position `i` of the first number and a digit in position `j` of the second lands in position `i + j + 1` of the result, with its carry going into `i + j`. Fill an array of `len(num1) + len(num2)` digits, then drop any leading zeros.

The numbers are never converted to integers, which the problem forbids and which would also hit Python's limit on huge integer-to-string conversions.

### Complexity

- Time: O(m * n).
- Space: O(m + n) for the digit array.
