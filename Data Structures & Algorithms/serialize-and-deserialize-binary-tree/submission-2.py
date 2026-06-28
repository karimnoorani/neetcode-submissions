# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []

        def dfs(node):
            if not node:
                preorder.append("N")
                return
            
            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(preorder)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        def buildTree(index):
            if data[index] == "N":
                return [None, index+1]
            
            node = TreeNode(val=int(data[index]))
            left, next_idx = buildTree(index+1)
            right, next_idx = buildTree(next_idx)
            node.left = left
            node.right = right
            return [node, next_idx]
        
        root, _ = buildTree(0)
        return root