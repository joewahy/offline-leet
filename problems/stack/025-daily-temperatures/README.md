# 25. Daily Temperatures (Medium)

`temperatures[i]` is the temperature on day `i`. Return a list `answer` where `answer[i]` is how many days you must wait after day `i` for a warmer temperature. If no warmer day ever comes, `answer[i]` is `0`.

## Examples

```
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Input:  temperatures = [30, 38, 30, 36, 35, 40, 28]
Output: [1, 4, 1, 2, 1, 0, 0]
```

## Constraints

- `1 <= len(temperatures) <= 10000`
- `30 <= temperatures[i] <= 100`

## Hints

- Keep a stack of days still waiting for a warmer day. When a warmer day arrives, pop everything it beats.
