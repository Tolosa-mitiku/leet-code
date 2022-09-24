# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return None, 0
            if not node.right and not node.left:
                return node.val, 1
            leftval, leftcount = helper(node.left)
            rightval, rightcount = helper(node.right)
            if node.val == leftval == rightval:
                ans = max(ans, leftcount + rightcount + 1)
                return node.val, max(leftcount, rightcount) + 1
            elif node.val == leftval:
                ans = max(ans, leftcount + 1)
                return node.val, leftcount + 1
            elif node.val == rightval:
                ans = max(ans, rightcount + 1)
                return node.val, rightcount + 1
            else:
                ans = max(ans, 1)
                return node.val, 1
        temp = helper(root)
        return ans - 1 if ans > 0 else 0