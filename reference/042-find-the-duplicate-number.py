class Solution:
    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow != slow2:
            slow, slow2 = nums[slow], nums[slow2]
        return slow
