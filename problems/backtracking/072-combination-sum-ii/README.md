# 72. Combination Sum II (Medium)

`candidates` is a list of positive integers that may contain duplicates, and `target` is a positive integer. Return every unique combination of candidates that adds up to `target`. Each candidate may be used at most once, and the result must not contain duplicate combinations.

The combinations, and the numbers inside them, may be returned in any order.

## Examples

```
Input:  candidates = [9, 2, 5, 2, 1], target = 9
Output: [[9], [2, 2, 5]]

Input:  candidates = [2, 5, 2, 1, 2], target = 5
Output: [[1, 2, 2], [5]]
```

## Constraints

- `1 <= len(candidates) <= 30`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Hints

- Sort the list. At each depth, skip a value that equals the previous one you already tried at that depth.
