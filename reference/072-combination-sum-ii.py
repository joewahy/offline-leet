class Solution:
    def combinationSum2(self, candidates, target):
        nums = sorted(candidates)
        out = []

        def go(start, remaining, path):
            if remaining == 0:
                out.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                go(i + 1, remaining - nums[i], path)
                path.pop()

        go(0, target, [])
        return out
