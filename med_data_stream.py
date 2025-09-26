#if length is odd, median is middle number, if even , med is average of two middle numbers
import heapq

class median_finder():
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num):
        heapq.push(self.small, -num)
        heapq.push(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findmedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0] // 2)