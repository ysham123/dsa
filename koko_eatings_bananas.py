class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += (p + k - 1) // k
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

        #T:O(n · log m), S:O(1)