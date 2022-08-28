"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                for i in curr.children:
                    queue.append(i)
            ans.append(temp)
        return ans