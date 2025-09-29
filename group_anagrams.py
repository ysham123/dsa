class Solution():
    def group_anagrams(self, strs:List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            store[key].append(word)
        return list(store.values())

        #Time:O(m*nlogn), Space:O(m*n)