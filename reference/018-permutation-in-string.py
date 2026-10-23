from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        n = len(s1)
        if n > len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[:n])
        if window == need:
            return True
        for i in range(n, len(s2)):
            window[s2[i]] += 1
            out = s2[i - n]
            window[out] -= 1
            if window[out] == 0:
                del window[out]
            if window == need:
                return True
        return False
