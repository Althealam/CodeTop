# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：
# 1. 先将链表从中间节点断开
# 2. 合并两个有序链表（注意需要建立虚拟头节点）
# 3. 返回最终合并后的链表

# 时间复杂度：O(nlogn)
# 空间复杂度：O(logn)
class Solution:
    def middleNode(self, head):
        """找到中间节点"""
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None
        return slow # slow为第二个链表的起始节点

    
    def mergeTwoLists(self, list1, list2):
        """合并两个有序链表"""
        dummy_node = ListNode()
        cur = dummy_node
        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy_node.next

     
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head2 = self.middleNode(head)
        head = self.sortList(head)
        head2 = self.sortList(head2)
        return self.mergeTwoLists(head, head2)
        

        

        