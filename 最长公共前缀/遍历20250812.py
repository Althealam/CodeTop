# 1. 初始化答案值为strs的第一个字符
# 2. 遍历strs[0]的每个字符，和strs中的其他字符进行判断，判断是否相同
# （1）如果相同，继续遍历strs[0]的下一个字符
# （2）如果不同，则说明已经找到了最大的公共前缀（st[i]!=ans[i]）
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i, ch in enumerate(ans): # 遍历行
            for st in strs: # 遍历列
                if i==len(st) or st[i]!=ans[i]:
                    return ans[:i]
        return ans
        