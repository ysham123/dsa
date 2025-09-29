class Solution():
    def topkfrequent(self, nums:List[int], k:int) -> List[int]:
        """from collections import Counter
        counter = Counter(nums)
        return[num for num, freq in counter.most_common(k)]""" #time: Time: O(n + u log k), Space:O(u)

        #The better approach

