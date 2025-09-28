class Solution():
    def threesum(self, nums:List[int]) -> List[List[int]]:
        res = []

        for x in range(len(nums)):
            for j in range(x+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[x] + nums[j] + nums[k] == 0:
                        triplets = sorted([nums[x], nums[j], nums[k]])
                        if triplets not in res:
                            res.append(triplets)
        return res

        