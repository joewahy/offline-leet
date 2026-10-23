class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
