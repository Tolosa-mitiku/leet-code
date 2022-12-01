# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True
            leftdepth, leftbalance = dfs(node.left)
            rightdepth, rightbalance = dfs(node.right)
            
            return 1 + max(leftdepth, rightdepth), abs(leftdepth - rightdepth) <= 1 and leftbalance and rightbalance
        return dfs(root)[1]
            