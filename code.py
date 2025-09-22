class Solution:
	def minCoins(self, coins, sum):
		# code here
        # cp = {}
        # def recur(coins, sum):
        #     if sum == 0:
        #         return 0
        #     if sum < 0:
        #         return float('inf')
        #     if sum in cp:
        #         return cp[sum]
                
        #     min_coins = float('inf')
        #     for coin in coins:
        #         ans = recur(coins, sum - coin)
        #         if ans != float('inf'):
        #             min_coins = min (ans +1, min_coins)
                    
        #     cp[sum] = min_coins
        #     return min_coins
     
        # result = recur(coins, sum)
        # if result == float('inf'):
        #     return -1
        # return result
        
        dp = [float('inf')]*(sum+1)
        dp[0] = 0
        
        for i in range(1, sum+1):
            for coin in coins:
                if i-coin >= 0:
                    ans = 1 + dp[i-coin]
                    dp[i] = min(dp[i], ans)
        if dp[sum] == float('inf'):
            return -1
        return dp[sum]
            