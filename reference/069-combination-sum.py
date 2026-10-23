class Solution:
    def combinationSum(self, nums, target):
        out = []

        def go(start, remaining, path):
            if remaining == 0:
                out.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] <= remaining:
                    path.append(nums[i])
                    go(i, remaining - nums[i], path)
                    path.pop()

        go(0, target, [])
        return out
