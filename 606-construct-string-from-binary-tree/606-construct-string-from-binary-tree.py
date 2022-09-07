# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(node):
            if not node:
                return ''
            s = str(node.val)
            if not node.left and not node.right:
                s += ''

            if node.left:
                s += '({})'.format(helper(node.left))
                
            if not node.left  and node.right:
                s += '()'

            if node.right:
                s += '({})'.format(helper(node.right))
            return s    
        
        return helper(root)