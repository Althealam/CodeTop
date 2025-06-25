# 思路：遇到左括号则入栈其对应的右括号，遇到右括号则弹出栈顶元素
# 三种不匹配的情况
# 1. 字符串里左括号多余，因此不匹配
# 2. 字符串里右括号多余，因此不匹配
# 3. 字符串里括号没有多余，但是括号的类型没有匹配上，因此不匹配

# 判断方法：
# 1. 如果遇到右括号时，弹出的栈顶元素和右括号不匹配，则为False（表示没有以正确顺序闭合）
# 2. 如果遇到右括号时，栈内已经为空了，则为False（表示该右括号没有合适的左括号）
# 3. 如果所有元素都遍历完了，栈内还不为空，则为False（表示左括号没有合适的右括号）
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for item in s:
            if item=='(':
                st.append(')')
            elif item=='[':
                st.append(']')
            elif item=='{':
                st.append('}')
            elif len(st)==0 or st[-1]!=item:  # 遍历过程中栈已经为空了，或者栈顶元素和当前遇到的元素不同
                return False
            else:
                st.pop() # 栈顶元素和当前遍历的item相同，则弹出栈顶元素
        return True if len(st)==0 else False