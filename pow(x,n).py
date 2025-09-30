class Solution():
    def mypow(self, x:float, n:int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.mypow(x,-n)
        half = self.mypow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x