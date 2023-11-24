# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        l1 = list1
        l2 = list2
        
        head = ListNode()
        curr = head
        
        while l1 is not None or l2 is not None:
            l1v = l1.val if l1 else 101
            l2v = l2.val if l2 else 101
            
            if l1v <= l2v:
                curr.next = ListNode(l1v)
                l1 = l1.next if l1 else None
            elif l2v < l1v:
                curr.next = ListNode(l2v)
                l2 = l2.next if l2 else None
        
            curr = curr.next

        return head.next