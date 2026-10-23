class PrefixTree:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def _find(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return None
            node = node[c]
        return node

    def search(self, word):
        node = self._find(word)
        return node is not None and "$" in node

    def startsWith(self, prefix):
        return self._find(prefix) is not None
