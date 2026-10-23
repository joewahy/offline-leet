# 65. Task Scheduler (Medium)

A CPU must run the tasks in `tasks`, each labelled with an uppercase letter. One task takes one unit of time, and in each unit the CPU either runs a task or sits idle. Tasks may be run in any order.

Between two runs of the same letter there must be at least `n` units in which that letter does not run (the CPU may run other tasks or idle in those units).

Return the minimum number of time units needed to finish every task.

## Examples

```
Input:  tasks = ["X", "X", "Y", "Y"], n = 2
Output: 5          # X Y _ X Y

Input:  tasks = ["A", "A", "A", "B", "B", "B"], n = 3
Output: 10         # A B _ _ A B _ _ A B
```

## Constraints

- `1 <= len(tasks) <= 10000`
- `0 <= n <= 100`
- Tasks are uppercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The task that appears most often is the bottleneck, because its copies need gaps between them.
2. Lay out the most frequent task with `n` slots between its copies. Other tasks fill those gaps, and idle time remains only if the gaps cannot be filled.
3. With `top` = highest count and `ties` = how many tasks have that count, the answer is `max(len(tasks), (top - 1) * (n + 1) + ties)`. Or simulate with a max-heap and a cooldown queue.

</details>
