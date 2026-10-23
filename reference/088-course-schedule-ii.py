from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        indeg = [0] * numCourses
        after = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            after[b].append(a)
            indeg[a] += 1
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for nxt in after[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return order if len(order) == numCourses else []
