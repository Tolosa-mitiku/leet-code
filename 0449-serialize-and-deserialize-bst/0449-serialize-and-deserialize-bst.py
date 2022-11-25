# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        string = []
        def preorder(node):
            if not node:
                string.append("#")
                string.append(",")
                return None
            string.append(str(node.val))
            string.append(",")
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return "".join(string)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        string = data.split(",")
        counter = -1
        
        def buildtree(string):
            nonlocal counter
            counter += 1
            if string[counter] == "#":
                return None
            node = TreeNode(int(string[counter]))
            node.left = buildtree(string)
            node.right = buildtree(string)
            return node
        
        return buildtree(string)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans