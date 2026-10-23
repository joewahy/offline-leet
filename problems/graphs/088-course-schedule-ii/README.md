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

- `1 <= numCourses <= 2000`
- `0 <= len(prerequisites) <= 3000`
- All pairs are distinct.

## Hints

- The order is a topological sort. If your sort cannot include every course, there is a cycle.
