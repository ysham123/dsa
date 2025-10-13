class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

        #time:O(n), space:O(1)