class Solution(object):
    def reverseWords(self, s):
        """return " ".join(reversed(s.split()))     ---fully optimal""" 

        #also optimal
        words = s.split()
        reversed_words = words[::-1]
        reversed_string = " ".join(reversed_words)
        return reversed_string 