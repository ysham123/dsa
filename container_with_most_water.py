class Solution():
    def containter_with_most_water(self,heights:List[int]) -> int:
        res = 0
        l,r = 0, len(heights) - 1

        while l < r:
            area = (heights[l], heights[r]) * (r-l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

        #Time: O(n), Space:O(1)