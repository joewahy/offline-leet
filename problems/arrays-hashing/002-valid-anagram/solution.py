class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1

        for char in t:
            if char not in dic:
                return False
            dic[char] -= 1
            if dic[char] == 0:
                del dic[char]
        
        if len(dic) == 0:
            return True
        return False