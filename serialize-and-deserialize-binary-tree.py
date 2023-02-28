# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
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
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))