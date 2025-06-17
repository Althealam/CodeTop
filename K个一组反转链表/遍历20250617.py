# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 反转逻辑：通过pre和cur逐节点反转，每次将cur指向pre，并更新指针位置
# 连接操作：
# （1）p0始终指向前一组的最后一个节点（初始为dummy_head）
# （2）p0.next.next=cur：将反转后的尾节点连接到当前cur（下一组的头节点）
# （3）p0.next=pre：将前一组的尾节点连接到反转后的新头节点
# 处理剩余节点：当剩余节点数不足K的时候，直接退出循环，保持原来的顺序

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 求出链表个数，每次反转之前判断剩余个数
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        
        # 2. 反转链表
        dummy_head = ListNode(next=head) # 虚拟头节点（头节点也有可能被反转）
        p0=dummy_head # p0是用来标记反转链表的开始节点的
        # 开始反转链表
        while n>=k: # n为链表剩余未反转的个数
            n-=k # 反转k个链表 
            pre=None # 当前反转的节点的上一个节点
            cur=p0.next # 当前正在遍历的节点，也是需要反转的起始节点

            # 反转k个节点
            for _ in range(k):
                nxt=cur.next # 记录当前节点的下一个节点
                cur.next=pre
                pre=cur
                cur=nxt
            
            # p0：前一组的最后一个节点（初始状态为虚拟头节点）
            # pre：反转后的新头节点（反转后段的第一个节点）
            # cur：反转后的尾节点的下一个节点（未反转部分的头节点）
            # nxt：当前反转段的原头节点（用于记录下一段起点）
            
            # 保存下一段要反转的链表的起始节点
            nxt=p0.next

            # 将反转后的链表和左边连接起来
            p0.next.next=cur
            # 将反转后的链表和右边连接起来
            p0.next=pre
            # 更新p0的值
            p0=nxt
        return dummy_head.next
