# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        for i in range(n):
            right = right.next
        if right == None:
            return head.next
        while right.next != None:
            left = left.next
            right = right.next

        temp = left.next.next
        left.next = temp
        return head