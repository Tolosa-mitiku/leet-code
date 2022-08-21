# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        sett = set()
        def helper(node, val):
            if not node:
                return
            node.val = val
            sett.add(val)
            helper(node.left,(val*2) + 1)
            helper(node.right, (val*2) + 2)
        helper(root, 0)
        self.nodes = sett

    def find(self, target: int) -> bool:
        if target in self.nodes:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)