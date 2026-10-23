# 13. Container With Most Water (Medium)

`heights[i]` is the height of a vertical line drawn at position `i`. Pick any two lines; together with the x-axis they form a container whose water level is limited by the shorter line.

Return the largest amount of water a container can hold (width times the shorter height).

## Examples

```
Input:  heights = [1, 7, 2, 5, 4, 7, 3, 6]
Output: 36

Input:  heights = [2, 2, 2]
Output: 4
```

## Constraints

- `2 <= len(heights) <= 12000`
- `0 <= heights[i] <= 10000`

## Hints

- Start with the widest container. Moving which pointer could ever help?
