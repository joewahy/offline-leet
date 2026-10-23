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

## Hints

- Process the tree one whole level at a time with a queue, using the queue's size at the start of each round.
