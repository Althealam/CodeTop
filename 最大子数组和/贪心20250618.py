# 贪心法：如果当前连续子数组的和小于0，则从下一个元素开始计算

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right = 0
        ans = float('-inf') # 最大子数组和
        sum_ = 0 # 计算当前滑动窗口的子数组和
        while right<len(nums):
            sum_+=nums[right]
            ans = max(ans, sum_)
            if sum_<0:
                sum_=0
            right+=1
        return ans
        
        