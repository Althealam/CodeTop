# 思路：
# 定义一个滑动窗口（使用双指针left和right）用来寻找不含重复字符的子串
# 定义一个dict来存储各个字符的出现次数
# right不断的向右边移动，直到滑动窗口内出现重复的字符，则将left的出现次数减去1，并且将left右移，直到滑动窗口内没有出现重复字符为止
# 每次移动right的时候都更新无重复字符的最长子串的答案值

s=str(input())
print(s)

from collections import defaultdict
def solution(s):
    left=0
    ans=0
    cnt=defaultdict(int)
    for right, ch in enumerate(s):
        cnt[ch]+=1
        while cnt[ch]>1:
            cnt[s[left]]-=1
            left+=1
        ans=max(ans, right-left+1)
    return ans

result=solution(s)
print(result)