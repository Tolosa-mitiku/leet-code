# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        counter = defaultdict(int)
        def helper(node):
            if not node:
                return 0
            counter[node.val] += 1
            if not node.left and not node.right:
                odds = 0
                for i in counter.values():
                    if int(i) % 2 == 1:
                        odds += 1
                counter[node.val] -= 1
                return 1 if odds < 2 else 0
            left = helper(node.left)
            right = helper(node.right)
            counter[node.val] -= 1
            return left + right
        return helper(root)
            