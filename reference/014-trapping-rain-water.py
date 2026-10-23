class Solution:
    def trap(self, height):
        i, j = 0, len(height) - 1
        left = right = water = 0
        while i < j:
            if height[i] < height[j]:
                left = max(left, height[i])
                water += left - height[i]
                i += 1
            else:
                right = max(right, height[j])
                water += right - height[j]
                j -= 1
        return water
