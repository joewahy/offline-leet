class Solution:
    def generateParenthesis(self, n):
        out = []

        def build(cur, opens, closes):
            if len(cur) == 2 * n:
                out.append(cur)
                return
            if opens < n:
                build(cur + "(", opens + 1, closes)
            if closes < opens:
                build(cur + ")", opens, closes + 1)

        build("", 0, 0)
        return out
