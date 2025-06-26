# 思路：维护一个最小的买入价格，维护一个最大利润即可
# 时间复杂度：O(n)
# 空间复杂度：O(1)
prices = list(map(int, input().split()))

def greedy(prices):
    min_price = prices[0] # 需要维护的最小买入价格
    ans = 0 # 最大利润
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        ans = max(ans, prices[i]-min_price)
    return ans
