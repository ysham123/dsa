class Solution():
    def is_anagram(self, s:str, t:str) -> bool:
        """
        brute force
        return sorted(s) == sorted(t)
        """

        #optimal Solution
        if len(s) != len(t):
            return False
        counts,countt = {},{}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            counts[t[i]] = 1 + countt.get(t[i], 0)

        return counts == countt

        #time: O(m+n), space: O(n)