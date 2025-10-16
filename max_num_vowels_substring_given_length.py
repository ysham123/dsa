class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        l = 0
        count = 0
        max_count = 0

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            # shrink window if size exceeds k
            if r - l + 1 > k:
                if s[l] in vowels:
                    count -= 1
                l += 1
            max_count = max(max_count, count)
        return max_count

        #time:O(n), Space:O(1)