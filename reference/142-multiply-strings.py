class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                total = res[i + j + 1] + (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                res[i + j + 1] = total % 10
                res[i + j] += total // 10
        start = 0
        while res[start] == 0:
            start += 1
        return "".join(map(str, res[start:]))
