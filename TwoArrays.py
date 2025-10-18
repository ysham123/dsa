class Solution(object):
    def findDifference(self, nums1, nums2):
        unique1 = list(set(nums1) - set(nums2))
        unique2 = list(set(nums2) - set(nums1))
        return [unique1, unique2]
#T:O(M+N), S:O(M+N)