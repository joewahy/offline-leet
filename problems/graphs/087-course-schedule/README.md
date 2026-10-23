# 87. Course Schedule (Medium)

You must take `numCourses` courses, labelled `0` to `numCourses - 1`. `prerequisites[i] = [a, b]` means you must take course `b` before course `a`.

Return `True` if it is possible to finish all courses, otherwise `False` (which happens when the prerequisites contain a cycle).

## Examples

```
Input:  numCourses = 2, prerequisites = [[0, 1]]
Output: True

Input:  numCourses = 2, prerequisites = [[0, 1], [1, 0]]
Output: False
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= len(prerequisites) <= 3000`
- All pairs are distinct.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Model courses as nodes and prerequisites as directed edges. When is it impossible to finish?
2. It is impossible exactly when the graph has a cycle.
3. Detect the cycle with a topological sort: repeatedly take courses with no remaining prerequisites (in-degree 0). If you can take all of them, there is no cycle. A DFS with a 'currently visiting' set also works.

</details>
