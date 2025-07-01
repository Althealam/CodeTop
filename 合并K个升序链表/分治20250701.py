# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(Llogm)，其中m为lists的长度，L为所有链表的长度之和。每个节点参与链表合并的次数为O(logm)次，一共有L个节点，所以总的时间复杂度为O(Llogm)
# 空间复杂度：O(logm)，递归深度为O(logm)，需要O(logm)的栈空间
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists) # 总共有m个链表
        if m==0:
            return None
        if m==1:
            return lists[0]
        mid = m//2 # 中间链表
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, list1, list2):
        """合并两个排序链表"""
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next