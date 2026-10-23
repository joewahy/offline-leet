class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def search(self, word):
        def go(node, i):
            if i == len(word):
                return "$" in node
            c = word[i]
            if c == ".":
                return any(go(child, i + 1) for key, child in node.items() if key != "$")
            return c in node and go(node[c], i + 1)

        return go(self.root, 0)
