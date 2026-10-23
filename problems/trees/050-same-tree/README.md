# 50. Same Tree (Easy)

Given the roots of two binary trees `p` and `q`, return `True` if they have exactly the same shape and the same value at every position, otherwise `False`.

## Examples

```
Input:  p = [1, 2, 3], q = [1, 2, 3]
Output: True

Input:  p = [4, 7], q = [4, null, 7]
Output: False
```

## Constraints

- `0 <= number of nodes in each tree <= 3000`
- `-100 <= node.val <= 100`

## Hints

- Two trees are the same when both are empty, or the roots match and both pairs of subtrees are the same.
