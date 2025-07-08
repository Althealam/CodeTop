# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        fast, slow = dummy_node, dummy_node
        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        # 此时slow到达了倒数第N个节点的前面一个节点
        slow.next = slow.next.next

        return dummy_node.next

