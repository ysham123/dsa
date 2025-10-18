class Solution(object):
    def moveZeroes(self, nums):
        j = 0

        for x in range(len(nums)):
            if nums[x] != 0:
                nums[x], nums[j] = nums[j], nums[x]
                j += 1

                #T:O(n), S:O(1)