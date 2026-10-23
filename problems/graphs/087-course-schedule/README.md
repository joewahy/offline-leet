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

## Hints

- Model courses as nodes and prerequisites as directed edges. The question is whether the graph has a cycle.
- Topological sorting (repeatedly take courses with no remaining prerequisites) detects cycles.
