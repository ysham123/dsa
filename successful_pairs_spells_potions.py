class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        res = []

        for s in spells:
            min_needed = (success + s - 1) // s
            # manual binary search
            l, r = 0, m
            while l < r:
                mid = (l + r) // 2
                if potions[mid] < min_needed:
                    l = mid + 1
                else:
                    r = mid
            res.append(m - l)
        return res
        #T:O(mlogm+nlogm), S:O(n)