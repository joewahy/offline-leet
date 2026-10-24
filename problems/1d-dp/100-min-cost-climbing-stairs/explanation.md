### Approach

The cheapest way to stand on step `i` is the cheaper of two options: arrive from step `i - 1` and pay its cost, or arrive from step `i - 2` and pay its cost. The top (one past the last step) is the goal, and you may start from step 0 or step 1 for free. Only the last two results are needed.

### Complexity

- Time: O(n).
- Space: O(1).
