# 1. dp数组以及下标的含义：dp[i]表示爬到第i个台阶时的方法总数
# 2. 递推公式：
# dp[i]=dp[i-1]+dp[i-2]
# 3. 初始化：全部初始化为0 dp[0]=1 dp[1]=1 dp[2]=2
# 4. 遍历顺序：从前向后遍历
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        if n<2:
            return 1
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]