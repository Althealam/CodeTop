# 思路：建议max-min的整数哈希表，不在nums里面的整数个数就是0，统计nums中每个元素的出现次数，通过遍历哈希表找到第K大的元素
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        MAX=max(nums)
        MIN=min(nums)
        hash_map={}
        # 倒序建立最大数到最小数的哈希表
        for i in range(MAX, MIN-1, -1):
            hash_map[i]=0
        # 计算每个元素的出现次数
        for num in nums:
            hash_map[num]+=1
        res = 0 # 统计现在的元素是第几个大的元素
        for i in hash_map:
            res+=hash_map[i]
            if res>=k: # 找到第K大的元素
                return i
        