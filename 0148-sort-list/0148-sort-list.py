# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        def mergeSortedArray(a, b):
            ans = head = ListNode()
            while a != None and b != None:
                if a.val <= b.val:
                    head.next = a
                    a = a.next
                else:
                    head.next = b
                    b = b.next
                head = head.next
            
            head.next = a or b
            return ans.next
        def mergeSort(head):
            if head.next != None:
                slow = fast = head
                
                temp = slow
                while fast != None and fast.next != None:
                    fast = fast.next.next
                    temp = slow
                    slow = slow.next
                temp.next = None
                    
                left = mergeSort(head)
                right = mergeSort(slow)
                ans = mergeSortedArray(left, right)
                return ans
                
            return head
        return mergeSort(head)