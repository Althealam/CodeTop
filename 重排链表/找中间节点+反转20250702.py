# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：
# 1. 找到中间节点
# 2. 反转第二段链表
# 3. 将两个链表拼接在一起

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找到中间节点
        middle_node = self.get_middle_node(head)
        # 反转第二段链表
        head2 = self.reverse_list(middle_node)
        # 拼接两段链表
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2

    def get_middle_node(self, head):
        """寻找中间节点"""
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow # slow到达的位置就是链表的中间节点
    
    def reverse_list(self, head):
        """反转链表"""
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre