# 1. 定义hashmap，统计nums中每个元素以及元素的出现次数
# 2. 遍历nums中的每个num，在hashmap中判断num+1是否出现过，并且依次遍历num+2
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        ans = 0 # 最长序列的长度
        for num in hash_nums:
            if num-1 in hash_nums:
                continue
            next_num = num+1
            while next_num in hash_nums: # 不断判断下一个数是否在哈希集合中
                next_num+=1
            ans = max(ans, next_num-num) # 获取本次连续序列的长度
        return ans
        