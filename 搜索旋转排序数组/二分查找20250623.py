# 分析：
# 1. 在第一段或者第二段中查找target
# （1）如果target>nums[n-1]，那么targert在第一段[0, i-1]中，在[0,i-1]中查找target
# （2）如果target<=nums[n-1]
# （2.1）i=0：nums是递增的，直接在[0,n-1]中二分查找
# （2.2）i>0：target一定在第二段[i, n-1]中，在[i, n-1]中二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = self.findmin(nums)
        if target>nums[-1]: # target在第一段
            return self.lower_bound(nums, -1, i, target)
        return self.lower_bound(nums, i-1, len(nums)-1, target) # target在第二段

    def lower_bound(self, nums, left, right, target):
        """有序数组中找target的下标"""
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]>=target:
                right = mid
            else:
                left = mid
        return right if nums[right]==target else -1
    
    def findmin(self, nums):
        """寻找旋转排序数组的最小值"""
        left = -1
        right = len(nums)-1
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]<nums[-1]: # 最小值在mid的左侧（mid现在在第二段，或者是只有一段）
                right = mid
            else: # 最小值在mid的右侧
                left = mid
        return right
        

        