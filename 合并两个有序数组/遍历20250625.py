# 思路：考虑到不能覆盖nums1原来的元素，因此考虑使用逆向双指针
# 定义双指针分别指向nums1和nums2的末尾，也就是m-1和n-1，分别判断nums1[m-1]和nums2[n-1]的值，将较大的值放在nums1[m+n-1]的位置，然后继续移动指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p0=m-1 # 指向nums1的指针
        p1=n-1 # 指向nums2的指针
        p2=m+n-1 # 指向最终数组的指针
        while p1>=0: # 只要nums2中还有元素没合并，就继续
            if p0>=0 and nums1[p0]>nums2[p1]: # nums1还有有效元素
                nums1[p2]=nums1[p0]
                p0-=1
            else:
                nums1[p2]=nums2[p1] # nums1无有效元素，或者nums2元素更大
                p1-=1
            p2-=1