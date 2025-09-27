class Solution():
    def twosum(nums, target):
        store = {}

        for x, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], x]
            store[num] = x


class Solution():
    def twosum(nums, target):
        prevmap = {}
        for x, num in enumerate(nums):
            diff = target - num
            if diff in prevmap:
                return [prevmap[diff], x]
            prevmap[num] = x