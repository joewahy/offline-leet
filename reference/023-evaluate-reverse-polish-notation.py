class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in "+-*/" and len(t) == 1:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    q = abs(a) // abs(b)
                    stack.append(q if (a < 0) == (b < 0) else -q)
            else:
                stack.append(int(t))
        return stack[0]
