# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        defdict = defaultdict(int)
        def helper(node):
            nonlocal ans
            defdict[node.val] += 1
            if not node.left and not node.right:
                print(defdict)
                odds = 0
                for i in defdict.values():
                    if int(i) % 2 == 1:
                        odds += 1
                ans += odds < 2
                defdict[node.val] -= 1
                return
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            defdict[node.val] -= 1
        helper(root)
        return ans
            