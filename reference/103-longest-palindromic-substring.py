class Solution:
    def longestPalindrome(self, s):
        best = ""
        for centre in range(2 * len(s) - 1):
            lo, hi = centre // 2, centre // 2 + centre % 2
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > len(best):
                best = s[lo + 1:hi]
        return best
