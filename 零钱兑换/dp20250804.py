# 1. dp数组以及下标的含义：dp[i]表示组合成金额为i时的最少的硬币个数为dp[i]
# 2. 递推公式：
# （1）使用coin：dp[i-coin]+1
# （2）不使用coin：dp[i]
# 3. 初始化：全部初始化为inf dp[0]=0
# 4. 遍历顺序：先遍历物品 后遍历背包
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i-coin]+1, dp[i])
        return dp[-1] if dp[-1]!=float('inf') else -1
            
        