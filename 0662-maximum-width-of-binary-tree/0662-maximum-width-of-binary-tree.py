# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        queue = deque([(root, 0)])
        while queue:
            for i in range(len(queue)):
                node, ind = queue.popleft()
                if node.left:
                    queue.append((node.left, (2 * ind) + 1))
                if node.right:
                    queue.append((node.right, (2 * ind) + 2))
            if queue:
                ans = max(ans, queue[-1][1] - queue[0][1] + 1)
        return ans