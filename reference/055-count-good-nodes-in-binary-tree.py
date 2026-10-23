class Solution:
    def goodNodes(self, root):
        def go(node, biggest):
            if not node:
                return 0
            good = node.val >= biggest
            biggest = max(biggest, node.val)
            return good + go(node.left, biggest) + go(node.right, biggest)

        return go(root, root.val)
