class Codec:
    def serialize(self, root):
        out = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                out.append("N")
            else:
                out.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
        return ",".join(out)

    def deserialize(self, data):
        tokens = iter(data.split(","))

        def build():
            tok = next(tokens)
            if tok == "N":
                return None
            node = TreeNode(int(tok))
            node.left = build()
            node.right = build()
            return node

        return build()
