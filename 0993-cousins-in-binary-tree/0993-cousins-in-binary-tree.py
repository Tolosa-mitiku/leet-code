# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        first = [0, 0]
        second = [0, 0]
        def dfs(node, parent, depth):
            if not node:
                return
            
            if node.val == x:
                first[0], first[1] = depth, parent
            elif node.val == y:
                second[0], second[1] = depth, parent
                
            dfs(node.left, node.val, depth+1)
            dfs(node.right, node.val, depth+1)
        dfs(root, -1, 0)
        
        if first[0] == second[0] and first[1] != second[1]:
            return True
        return False