class Solution():
    def coinchange(coins, amount):
        if amount == 0:
            return 0
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if (a-c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return -1 if dp[amount] == INF else dp[amount] 
#Time:O(n * t), Space:O(t)