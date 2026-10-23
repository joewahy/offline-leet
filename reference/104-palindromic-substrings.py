class Solution:
    def countSubstrings(self, s):
        count = 0
        for centre in range(2 * len(s) - 1):
            lo, hi = centre // 2, centre // 2 + centre % 2
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1
        return count
