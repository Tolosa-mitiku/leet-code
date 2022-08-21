# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph= defaultdict(list)
        def helper(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            left = helper(node.left)
            right = helper(node.right)
        helper(root)
        
        visited = set()
        queue = deque([start])
        ans = 0
        while queue:
            ans += 1
            for j in range(len(queue)):
                curr = queue.popleft()
                visited.add(curr)
                for i in graph[curr]:
                    if i not in visited:
                        queue.append(i)
                
        print(graph)
        return ans-1