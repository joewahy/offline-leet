from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        groups = defaultdict(list)
        for w in set(wordList) | {beginWord}:
            for i in range(len(w)):
                groups[w[:i] + "*" + w[i + 1:]].append(w)
        seen = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for i in range(len(w)):
                for n in groups[w[:i] + "*" + w[i + 1:]]:
                    if n not in seen:
                        seen.add(n)
                        q.append((n, d + 1))
        return 0
