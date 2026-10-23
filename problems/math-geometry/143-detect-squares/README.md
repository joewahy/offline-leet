# 143. Detect Squares (Medium)

Design a data structure that receives points on a 2D plane and counts axis-aligned squares.

Implement `DetectSquares`:

- `DetectSquares()` creates an empty structure.
- `add(point)` adds the point `[x, y]`. The same point may be added several times; each copy counts separately.
- `count(point)` returns the number of ways to choose three stored points that, together with the query `point`, form a square with positive area whose sides are parallel to the axes.

## Examples

```
add([3, 10]); add([11, 2]); add([3, 2])
count([11, 10])  -> 1
count([14, 8])   -> 0
add([11, 2])
count([11, 10])  -> 2
```

## Constraints

- `0 <= x, y <= 1000`
- At most `3000` calls are made.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A square is fixed by the query point and the point diagonally opposite it. Which other two corners follow?
2. Keep a count of each distinct point. For each stored point on a diagonal of the query, check the other two corners.
3. A stored point `(px, py)` is a valid opposite corner when `abs(px - x) == abs(py - y)` and `px != x`. The other corners are `(px, y)` and `(x, py)`. Add `count(px, py) * count(px, y) * count(x, py)` to the answer.

</details>
