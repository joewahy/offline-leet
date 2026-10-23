class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        out = []

        def go(start, path):
            out.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                go(i + 1, path)
                path.pop()

        go(0, [])
        return out
