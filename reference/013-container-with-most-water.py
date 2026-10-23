class Solution:
    def maxArea(self, heights):
        i, j = 0, len(heights) - 1
        best = 0
        while i < j:
            best = max(best, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return best
