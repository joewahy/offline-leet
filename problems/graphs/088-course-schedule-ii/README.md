# 88. Course Schedule II (Medium)

You must take `numCourses` courses, labelled `0` to `numCourses - 1`. `prerequisites[i] = [a, b]` means you must take course `b` before course `a`.

Return an order in which you can take all the courses. If several orders work, return any one of them. If it is impossible (there is a cycle), return an empty list.

## Examples

```
Input:  numCourses = 2, prerequisites = [[1, 0]]
Output: [0, 1]

Input:  numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3]      # [0, 2, 1, 3] is also accepted
```

## Constraints

- `1 <= numCourses <= 10^5`
- `0 <= len(prerequisites) <= 10^5`
- All pairs are distinct.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. This is the previous problem, but you must also output an order.
2. A valid order is a topological ordering of the graph.
3. Run Kahn's algorithm: start with the courses of in-degree 0, append each one to the order, and decrease the in-degree of the courses that depend on it. If the order has fewer than `numCourses` entries, return `[]`.

</details>
