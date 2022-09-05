"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def helper(node):
            if not node:
                return
            ans.append(node.val)
            for i in node.children:
                helper(i)
        helper(root)
        return ans