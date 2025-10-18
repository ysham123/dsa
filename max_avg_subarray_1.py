class Solution(object):
    def findMaxAverage(self, nums, k):
        max_sum = float('-inf')
        current_sum = 0
        l = 0

        for r in range(len(nums)):
            current_sum += nums[r]

            while r-l + 1 > k:
                current_sum -= nums[l]
                l += 1
            if r-l + 1 == k:
                max_sum = max(max_sum, current_sum)
        return float(max_sum) / k
#Time:O(n), Space:O(1)