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

- `1 <= len(heights) <= 10^5`
- `0 <= heights[i] <= 10000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. For any bar, the best rectangle that uses its full height extends left and right until it meets a shorter bar.
2. So for each bar you need the nearest shorter bar on each side. A stack of increasing heights finds those in one pass.
3. Keep a stack of `(start_index, height)`. When a new bar is shorter, pop the taller bars, compute `height * (i - start)` for each, and give the new bar the earliest `start` among the popped ones. Append a `0` bar at the end to flush the stack.

</details>
