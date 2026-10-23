from collections import deque


class Solution:
    def rightSideView(self, root):
        out = []
        q = deque([root] if root else [])
        while q:
            out.append(q[-1].val)
            for _ in range(len(q)):
                node = q.popleft()
                q.extend(c for c in (node.left, node.right) if c)
        return out
