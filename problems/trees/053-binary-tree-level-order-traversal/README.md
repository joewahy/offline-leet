# 53. Binary Tree Level Order Traversal (Medium)

Return the level order traversal of a binary tree: a list of lists, where the `i`-th list holds the values of all nodes at depth `i`, from left to right.

## Examples

```
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

Input:  root = [1]
Output: [[1]]
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-1000 <= node.val <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You want to visit the tree one level at a time, not depth first. Which structure visits nodes in the order they were discovered?
2. Use a queue (breadth-first search), starting with the root.
3. In each round, take `len(queue)` nodes (exactly one level), record their values in one list, and enqueue their children. Use `collections.deque` for O(1) pops from the front.

</details>
