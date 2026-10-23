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

## Hints

- The visible node on each level is the last one in a left-to-right level order traversal.
