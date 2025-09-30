#hard
import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (store as negatives)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # push to max heap
        heapq.heappush(self.small, -num)
        # balance by moving the largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # maintain size property
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2