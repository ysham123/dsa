class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        rob1,rob2 = 0,0
        for num in nums:
            next_rob = max(rob2, num + rob1)
            rob1 = rob2
            rob2 = next_rob
        return rob2