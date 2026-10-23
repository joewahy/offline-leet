# 58. Construct Binary Tree from Preorder and Inorder Traversal (Medium)

You are given the preorder and the inorder traversal of a binary tree whose node values are all distinct. Rebuild the tree and return its root.

(Preorder visits root, left subtree, right subtree. Inorder visits left subtree, root, right subtree.)

## Examples

```
Input:  preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]

Input:  preorder = [1, 2], inorder = [1, 2]
Output: [1, null, 2]
```

## Constraints

- `1 <= len(preorder) == len(inorder) <= 3000`
- `-3000 <= value <= 3000`, all distinct

## Hints

- The first preorder value is the root. Find it in the inorder list to learn how many nodes belong to the left subtree.
- Store inorder positions in a dictionary so each lookup is O(1).
