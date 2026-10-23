class Solution:
    def isValidBST(self, root):
        def ok(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return ok(node.left, low, node.val) and ok(node.right, node.val, high)

        return ok(root, float("-inf"), float("inf"))
