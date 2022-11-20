# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftsearch(self, target, nums):
        left, right, best = 0, len(nums)-1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
                best = mid
            else:
                right = mid - 1
        return nums[best] if best != -1 else -1
    def rightsearch(self, target, nums):
        left, right, best = 0, len(nums)-1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
        return nums[best] if best != -1 else -1
    
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nodes = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            nodes.append(node.val)
            helper(node.right)
        helper(root)
        
        ans = []
        for i in range(len(queries)):
            ans.append([self.leftsearch(queries[i], nodes), self.rightsearch(queries[i], nodes)])
        return ans