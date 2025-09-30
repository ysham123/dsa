class Solution():
    def mypow(self, x:float, n:int) -> float:
        """if n == 0:
            return 1
        if n < 0:
            return 1 / self.mypow(x,-n)
        half = self.mypow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x"""
        #iterative solution, better O(1) space
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        while n > 0:
            if n % 2 == 1: # if n is odd
                res  *= x
            x *= x #square the base
            n //= 2 #half the exponent
        return res

        