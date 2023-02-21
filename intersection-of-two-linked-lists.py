# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left = headA
        right = headB
        count1 = 0
        count2 = 0
        while left != None:
            count1 += 1
            left = left.next
        while right != None:
            count2 += 1
            right = right.next
        
        if count1 > count2:
            pointer1 = headA
            for i in range(count1 - count2):
                pointer1 = pointer1.next
            
            while headB != None:
                if pointer1 == headB:
                    return pointer1
                headB = headB.next
                pointer1 = pointer1.next
        else:
            pointer1 = headB
            for i in range(count2 - count1):
                pointer1 = pointer1.next
            
            while headA != None:
                if pointer1 == headA:
                    return pointer1
                headA = headA.next
                pointer1 = pointer1.next
        return None