# 54. Binary Tree Right Side View (Medium)

Imagine standing to the right of a binary tree and looking at it. Return the values of the nodes you can see, ordered from top to bottom.

## Examples

```
Input:  root = [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]

Input:  root = [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 7]
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. At each depth, which node would you see from the right?
2. It is the last node of each level, in left-to-right order.
3. Do a level order traversal and take the last value of every level. Or do a DFS that visits the right child first and records a node's value the first time it reaches a new depth.

</details>
