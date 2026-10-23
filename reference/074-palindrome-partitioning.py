class Solution:
    def partition(self, s):
        out = []

        def go(start, path):
            if start == len(s):
                out.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1]:
                    path.append(piece)
                    go(end, path)
                    path.pop()

        go(0, [])
        return out
