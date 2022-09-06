# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node.left and not node.right:
                return node.val
            
            left = 0
            if node.left:
                left = helper(node.left)
                if not left:
                    node.left = None
            right = 0
            if node.right:
                right = helper(node.right)
                if not right:
                    node.right = None
            return (left or right) or node.val
        if not helper(root):
            return None
        return root
            