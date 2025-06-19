# 时间复杂度：O(nlogn) 
# （1）分区操作：遍历整个数组三次（分别构建left、middle、right），时间为O(n)
# （2）将数组分为三个部分：O(nlogn)（递归树）
# 空间复杂度：O(n)
# （1）递归栈空间：递归深度为O(logn)
# （2）额外数组空间：递归创建三个新列表
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        pivot = nums[mid]
        left = [x for x in nums if x<pivot]
        middle = [x for x in nums if x==pivot]
        right = [x for x in nums if x>pivot]
        return self.sortArray(left)+middle+self.sortArray(right)