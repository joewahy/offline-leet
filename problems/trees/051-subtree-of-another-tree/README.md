# 51. Subtree of Another Tree (Easy)

Given the roots of two binary trees `root` and `subRoot`, return `True` if `root` contains a node whose subtree (that node and all its descendants) is identical to `subRoot`, otherwise `False`.

## Examples

```
Input:  root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
Output: True

Input:  root = [1, 2, 3], subRoot = [1, 2]
Output: False
```

## Constraints

- `1 <= number of nodes in root <= 2000`, `1 <= number of nodes in subRoot <= 1000`
- `-100 <= node.val <= 100`

## Hints

- For each node of `root`, check whether the tree starting there is the same as `subRoot`.
