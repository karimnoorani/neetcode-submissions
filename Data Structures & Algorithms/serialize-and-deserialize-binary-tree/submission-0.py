# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(root):
            if root is None:
                res.append("N")
            else:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')

        def createTree(i):
            if preorder[i] == "N":
                return [None, i+1]

            root = TreeNode(int(preorder[i]))
            root.left, rightIndex = createTree(i+1)
            root.right, nextIndex = createTree(rightIndex)

            return [root, nextIndex]
        
        return createTree(0)[0]