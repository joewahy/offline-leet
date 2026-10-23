from collections import deque


class Solution:
    def levelOrder(self, root):
        out = []
        q = deque([root] if root else [])
        while q:
            out.append([])
            for _ in range(len(q)):
                node = q.popleft()
                out[-1].append(node.val)
                q.extend(c for c in (node.left, node.right) if c)
        return out
