class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        out = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    out.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return out
