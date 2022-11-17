# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pq = [p,q]
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            if sum([left, right, node in pq]) == 2:
                ans = node
            return left or right or (node in pq)
        helper(root)
        return ans