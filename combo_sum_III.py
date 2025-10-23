class Solution(object):
    def combinationSum3(self, k, n):
        res = []

        def backtrack(start, combo, total):
            if len(combo) == k and total == n:
                res.append(list(combo))
                return 
            if len(combo) >= k or total > n:
                return
            
            for i in range(start, 10):
                combo.append(i)
                backtrack(i + 1, combo, total + i)
                combo.pop()
        backtrack(1, [], 0)
        return res

        #T:O(C(9,k)), S:O(k)