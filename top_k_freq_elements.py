class Solution():
    def topkfrequent(self, nums:List[int], k:int) -> List[int]:
        """from collections import Counter
        counter = Counter(nums)
        return[num for num, freq in counter.most_common(k)]""" #time: Time: O(n + u log k), Space:O(u)

        #The better approach
        freq_map = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        res = []
        for freq in range(len(buckets) -1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res      #time:O(n), space:O(n)