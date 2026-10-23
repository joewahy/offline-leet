from collections import deque


class Solution:
    def foreignDictionary(self, words):
        after = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in after}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a.startswith(b):
                return ""
            for x, y in zip(a, b):
                if x != y:
                    if y not in after[x]:
                        after[x].add(y)
                        indeg[y] += 1
                    break
        q = deque(c for c in sorted(indeg) if indeg[c] == 0)
        out = []
        while q:
            c = q.popleft()
            out.append(c)
            for n in sorted(after[c]):
                indeg[n] -= 1
                if indeg[n] == 0:
                    q.append(n)
        return "".join(out) if len(out) == len(after) else ""
