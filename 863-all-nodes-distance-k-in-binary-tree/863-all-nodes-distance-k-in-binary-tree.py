# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def create_graph(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            create_graph(node.left)
            create_graph(node.right)
        create_graph(root)
        print(graph)
        visited = set()
        queue = deque([target.val])
        ans = []
        count = 0
        while queue:
            if count == k:
                ans = list(queue)
            count += 1
            for j in range(len(queue)):
                curr = queue.popleft()
                visited.add(curr)
                for i in graph[curr]:
                    if i not in visited:
                        queue.append(i)
        return ans
                    
        