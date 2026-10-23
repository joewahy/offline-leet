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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. For each day you want the next warmer day. Checking every later day is O(n^2). What is waiting for an answer at any moment?
2. Keep a stack of days that have not found a warmer day yet. Their temperatures are non-increasing from bottom to top.
3. For each new day, while the top of the stack is colder, pop it and set its answer to `today - popped_index`. Then push today. Each day is pushed and popped once, so it is O(n).

</details>
