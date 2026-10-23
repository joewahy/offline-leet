class Solution:
    def rob(self, nums):
        def line(xs):
            skip, take = 0, 0
            for x in xs:
                skip, take = max(skip, take), skip + x
            return max(skip, take)

        if len(nums) == 1:
            return nums[0]
        return max(line(nums[1:]), line(nums[:-1]))
