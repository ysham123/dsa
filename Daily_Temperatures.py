class Solution():
    def Daily_Temperatures(self,temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for x in range(len(temperatures)):
            while len(stack) > 0 and temperatures[x] > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = x-i
            stack.append(x)
        return res

        #Time:O(n), Space:O(n)