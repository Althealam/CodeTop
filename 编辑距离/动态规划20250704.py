# 1. dp数组以及下标的含义：dp[i][j]表示以word1[i-1]为下标的字符串要变成以word2[j-1]为下标的字符串需要的最少操作数是dp[i][j]
# 2. 递推公式：
# （1）word1[i-1]==word2[j-1]: dp[i][j]=dp[i-1][j-1]
# （2）word1[i-1]!=word2[j-1]
# （2.1）删除word1[i-1]的一个元素/增加word2[j-1]的一个元素/替换word1[i-1]或者word2[j-1]的一个元素：dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1[j-1]])+1
# 注意：
# （2.1.1）word1删除一个元素：dp[i-1][j]+1
# （2.1.2）word2删除一个元素：dp[i][j-1]+1
# （2.1.3）替换word1/word2: dp[i-1][j-1]+1
# 3. 初始化：word1[i][0]=i word2[0][j]=j
# 4. 遍历顺序：从前向后遍历
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp =[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0]=i
        for j in range(len(word2)+1):
            dp[0][j]=j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[-1][-1]
