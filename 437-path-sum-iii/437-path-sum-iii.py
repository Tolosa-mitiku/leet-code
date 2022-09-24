# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def helper(node, lst):
            nonlocal ans
            if not node:
                return
            
            lst.append(node.val)
            count = 0
            for i in range(len(lst)-1, -1,-1):
                count += lst[i]
                if count == targetSum:
                    ans += 1
            if not node.right and not node.left:
                lst.pop()
                return
            helper(node.left, lst)
            helper(node.right, lst)
            lst.pop()
        
        helper(root, [])
        return ans