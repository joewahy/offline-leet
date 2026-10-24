### Approach

The answer at index `i` is the product of everything to its left times everything to its right. Compute those separately in two passes, with no division.

The first pass walks left to right and stores in `out[i]` the product of all earlier elements. The second pass walks right to left and multiplies `out[i]` by the product of all later elements, which it keeps in a running variable.

### Complexity

- Time: O(n), two passes.
- Space: O(1) extra. The output array does not count, and the two running products are single numbers.

### Watch out

Dividing the total product by `nums[i]` fails when the list contains a zero, and the problem forbids it.
