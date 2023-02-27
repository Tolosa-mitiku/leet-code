"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp:
            copy = Node(temp.val)
            copy.next = temp.next
            temp.next = copy
            temp = copy.next

        temp = head
        while temp:
            temp.next.random = temp.random and temp.random.next
            temp = temp.next.next

        temp = head
        copy = dummy = head and head.next
        while temp:
            temp.next = temp = copy.next
            copy.next = copy = temp and temp.next

        return dummy