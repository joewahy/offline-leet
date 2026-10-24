### Approach

Count how many times each point was added. To count squares for a query point `(x, y)`, treat each stored point `(px, py)` that is diagonal to it (same horizontal and vertical distance, not zero) as the opposite corner. The other two corners must be `(px, y)` and `(x, py)`. The number of squares using that corner is the product of how many copies of each of the three points exist.

### Complexity

- Time: O(1) per `add`, O(P) per `count`, where `P` is the number of distinct points.
- Space: O(P).

### Watch out

Duplicate points count separately, which is why the answer multiplies counts instead of checking for existence.
