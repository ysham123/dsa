from sys import prefix


class Solution():
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))
        prefix = 1
        for x in range(len(nums)):
            res[x] = prefix
            prefix *= nums[x]
        postfix = 1
        for x in range(len(nums) -1,-1,-1):
            res[x] *= postfix
            postfix *= nums[x]
        return res

    #we want each res[i] to hold the product of all elemetns before index i 

    nums = [1,2,3,4]
    res = [1,1,1,1]
    prefix = 1
    #forward pass
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    # now we need to multiply by the product of all elements after index i

    postfix = 1
    #backward pass

    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]

    """
    the forward loop fills in product of elemtns before i
    the backward loop multiplies in products of elemnts after i
    together each index gets everything except self
    """