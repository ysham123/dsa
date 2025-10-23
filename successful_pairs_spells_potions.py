class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        res = []

        for s in spells:
            min_needed = (success + s - 1) // s
            idx = bisect.bisect_left(potions, min_needed)
            res.append(m - idx)
        return res

        #T:O(mlogm+nlogm), S:O(n)