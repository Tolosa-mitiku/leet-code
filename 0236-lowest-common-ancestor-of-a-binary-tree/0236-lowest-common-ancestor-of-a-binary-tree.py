# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node, pq):
        if not node:
            return (False, None)
        left = self.helper(node.left, pq)
        right = self.helper(node.right, pq)
        ans = None
        if sum([left[0], right[0], node in pq]) == 2:
            ans = node
        return (left[0] or right[0] or (node in pq), ans or left[1] or right[1])
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, [p,q])[1]
        
