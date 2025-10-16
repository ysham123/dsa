class Solution(object):
    def maxProfit(self, prices, fee):
        hold = -prices[0]
        cash = 0

        for price in prices:
            cash = max(cash, hold + price-fee)
            hold = max(hold, cash-price)
        return cash
    #time:O(n), Space:O(1)