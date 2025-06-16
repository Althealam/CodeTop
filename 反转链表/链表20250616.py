class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


class Solution:
    def reverseList(self, head):
        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current=current.next
    return dummy.next

def linkedlist_to_list(head):
    result=[]
    current = head
    while current:
        result.append(current.val)
        current=current.next
    return result

if __name__=='__main__':
    input_list=list(map(int, input().split()))

    sol = Solution()
    reversed_head = sol.reverseList(list_to_linkedlist(input_list))

    reversed_list = linkedlist_to_list(reversed_head)

    print(reversed_list)