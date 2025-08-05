# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(cnt):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

        