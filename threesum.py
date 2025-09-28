class Solution():
    def threesum(self, nums:List[int]) -> List[List[int]]:
        """res = []

        for x in range(len(nums)):
            for j in range(x+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[x] + nums[j] + nums[k] == 0:
                        triplets = sorted([nums[x], nums[j], nums[k]])
                        if triplets not in res:
                            res.append(triplets)
        return res

        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = sorted[nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]"""


        #optimal

        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue 
            l,r = i+1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

        #Time: O(n^2), Space:O(1, O(m) for output list)