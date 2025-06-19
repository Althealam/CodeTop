# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：定义两个指针idx_1和idx_2，分别指向两个链表的节点，将较小的节点值添加到结果里
# 时间复杂度：O(n+m)
# 空间复杂度：O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        nxt = dummy_head
        while list1 or list2:
            if list1 is not None and list2 is not None and list1.val<=list2.val:
                nxt.next = list1
                list1 = list1.next
            elif list1 is not None and list2 is not None and list1.val>list2.val:
                nxt.next = list2
                list2 = list2.next
            elif list1 is None and list2 is not None:
                nxt.next = list2
                list2 = list2.next
            elif list1 is not None and list2 is None:
                nxt.next = list1
                list1 = list1.next
            nxt = nxt.next
        return dummy_head.next