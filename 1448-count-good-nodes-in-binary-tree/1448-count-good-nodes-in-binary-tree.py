# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def helper(node, maxx):
            nonlocal ans
            if not node:
                return
            if node.val >= maxx:
                maxx = node.val
                ans += 1
            helper(node.left, maxx)
            helper(node.right, maxx)
        helper(root, float("-inf"))
        return ans