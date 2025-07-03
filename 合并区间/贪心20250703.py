# 思路：
# 1. 区间按照左边界升序排序
# 2. 将第一个区间放入到stack中
# 3. 每次遍历其他区间的时候，都和栈内的栈顶元素做比较，如果栈顶元素和区间内的元素有重合，则弹出栈顶元素，合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0]<=stack[-1][1]:
                intervals[i][0]=min(intervals[i][0], stack[-1][0])
                intervals[i][1]=max(intervals[i][1], stack[-1][1])
                stack.pop()
            stack.append(intervals[i])
        return stack