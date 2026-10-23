# 111. Unique Paths (Medium)

A robot stands in the top-left cell of an `m x n` grid and wants to reach the bottom-right cell. It can only move right or down.

Return the number of different paths the robot can take.

## Examples

```
Input:  m = 3, n = 6
Output: 21

Input:  m = 3, n = 3
Output: 6
```

## Constraints

- `1 <= m, n <= 100`
- The answer fits in a 32-bit integer for the tested sizes.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. To reach a cell you must come from the cell above it or the cell to its left.
2. So the number of ways to a cell is the sum of the ways to those two cells. The first row and first column each have one way.
3. Keep one row of the table and update it row by row: `row[j] += row[j - 1]`. It is also the binomial coefficient `C(m + n - 2, m - 1)`.

</details>
