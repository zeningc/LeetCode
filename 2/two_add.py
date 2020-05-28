# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c=0
        head=ListNode(None)
        cur=head
        while l1 or l2:
            n1=l1.val if l1 else 0
            n2=l2.val if l2 else 0
            sum=n1+n2+c
            c=1 if sum>=10 else 0
            node=ListNode(sum%10)
            cur.next=node
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if c==1:
            cur.next=ListNode(1)
        return head.next
            