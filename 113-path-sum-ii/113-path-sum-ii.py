# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def helper(node, lst):
            if not node:
                return
            lst.append(node.val)
            if not node.right and not node.left:
                if sum(lst) == targetSum:
                    ans.append(list(lst))
                    lst.pop()
                    return
            helper(node.left, lst)
            helper(node.right, lst)
            lst.pop()
        
        helper(root, [])
        return ans