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

## Hints

- Keep a count of each distinct point. For a query, try every stored point on the same diagonal and multiply the counts of the other two corners.
