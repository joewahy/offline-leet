class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        copies = {node: Node(node.val)}
        stack = [node]
        while stack:
            cur = stack.pop()
            for n in cur.neighbors:
                if n not in copies:
                    copies[n] = Node(n.val)
                    stack.append(n)
                copies[cur].neighbors.append(copies[n])
        return copies[node]
