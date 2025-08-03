# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代法：初始化答案为一个空链表，每次循环，向该链表末尾添加一个节点
# 循环遍历链表l1和l2，每次把两个节点值l1.val和l2.val与进位值carry相加，除以10的余数就是当前节点需要保存的位数，除以10的商就是新的进位值

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    # l1和l2为当前遍历的节点，carry为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0 # 进位值
        while l1 or l2 or carry: # 有一个不是空节点，或者还有进位，则继续迭代
            if l1:
                carry+=l1.val # 节点值和进位值加载一起
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            carry //=10 # 新的进位
            cur = cur.next
        return dummy.next