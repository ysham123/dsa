class Solution(object):
    def isSubsequence(self, s, t):
        l, r = 0,0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1     
            r += 1         

        return l == len(s)  

        #time: O(n), Space: O(1)