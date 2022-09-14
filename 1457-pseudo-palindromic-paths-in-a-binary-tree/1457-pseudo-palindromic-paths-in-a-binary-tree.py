# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def helper(node, count):
            if not node:
                return 0
            count ^= (1<<node.val)
            if not node.left and not node.right:
                return 0 if count & (count-1) else 1
            left = helper(node.left, count)
            right = helper(node.right, count)
            return left + right
        return helper(root,0)
            