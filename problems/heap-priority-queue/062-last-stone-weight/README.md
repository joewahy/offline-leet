# 62. Last Stone Weight (Easy)

You have a pile of stones with the given positive weights. Repeat this until at most one stone is left: take the two heaviest stones `x <= y` and smash them together.

- If `x == y`, both stones are destroyed.
- Otherwise the stone of weight `x` is destroyed and the other becomes weight `y - x`.

Return the weight of the last remaining stone, or `0` if none remain.

## Examples

```
Input:  stones = [2, 3, 6, 2, 4]
Output: 1

Input:  stones = [1, 2]
Output: 1
```

## Constraints

- `1 <= len(stones) <= 1000`
- `1 <= stones[i] <= 1000`

## Hints

- You repeatedly need the largest elements. A max-heap (use negated values with `heapq`) is the natural fit.
