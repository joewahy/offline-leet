# 27. Largest Rectangle in Histogram (Hard)

`heights[i]` is the height of the `i`-th bar in a histogram. Every bar is 1 unit wide and the bars touch each other.

Return the area of the largest rectangle that fits entirely inside the histogram.

## Examples

```
Input:  heights = [7, 1, 7, 2, 2, 4]
Output: 8          # the bars 7, 2, 2, 4 with height 2

Input:  heights = [1, 3, 7]
Output: 7
```

## Constraints

- `1 <= len(heights) <= 8000`
- `0 <= heights[i] <= 10000`

## Hints

- For each bar, how far can a rectangle of that bar's height extend left and right?
- A stack of increasing heights finds those boundaries in one pass.
