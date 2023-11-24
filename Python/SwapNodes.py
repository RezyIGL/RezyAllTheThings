# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapNodes(self, head, k: int):
        lList = []
        i = head

        while i is not None:
            iv = i.val if i else None
            lList.append(iv)
            i = i.next

        lList[k-1], lList[-k] = lList[-k], lList[k-1]
        head = ListNode()
        curr = head

        for i in lList:
            curr.next = ListNode(i)
            curr = curr.next
        
        return head.next