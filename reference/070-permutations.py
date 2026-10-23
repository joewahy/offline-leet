class Solution:
    def permute(self, nums):
        out = []

        def go(path, rest):
            if not rest:
                out.append(path)
                return
            for i in range(len(rest)):
                go(path + [rest[i]], rest[:i] + rest[i + 1:])

        go([], nums)
        return out
