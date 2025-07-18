# 思路：二分法，找到mid*mid<=x的地方，直到left和right重合（x的平方根一定在[0, x]之间）

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left<=right:
            mid = (left+right)//2
            if mid*mid>x:
                right = mid-1
            elif mid*mid<x:
                left = mid+1
            else:
                return mid
        return right
        

        