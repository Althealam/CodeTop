# 1. 定义单调栈（单调栈是单调递减的），栈中存储还没找到右边第一个比i更大的元素的元素下标i
# 2. 遍历数组
# （1）如果找到了比i更大的元素下标right，那么弹出栈顶元素，并且找到了right_max；此时如果stack不为空，那么left_max=stack[-1]
# （2）如果没有找到比i更大的元素下标right，则继续加入i，此时单调栈保持单调递减的状态
# 3. 计算当前水柱的体积：
# （1）height=min(right_max_height, left_max_height)-bottom_height
# （2）lenght = i-left_max-1（注意这里是给i找到可以存储水的水柱，所以不是right_max-i-1）
# 4. 计算ans：ans+=height*length

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]: # 找到了右边的第一个最大元素
                right_max = i
                bottom = stack.pop()
                if len(stack)==0:
                    break
                left_max = stack[-1]
                h = min(height[left_max], height[right_max])-height[bottom]
                l = i-left_max-1
                ans+=h*l
            stack.append(i)
        return ans