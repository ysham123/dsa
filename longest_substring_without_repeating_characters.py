from re import L


class Solution():
    def lengthoflongestsubstring(s):
        res = 0
        l = 0
        track = set()


        for r in range(len(s)):
            while s[r] in track:
                track.remove(s[l])
                l += 1
            track.add(s[r])
            res = max(res, r-l + 1)
        return res

        #time o(n), space o(m)