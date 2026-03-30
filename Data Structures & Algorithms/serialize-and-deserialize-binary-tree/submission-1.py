# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N"
        
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        def dfs(i):
            if data[i] == 'N':
                return [None, i+1]
            
            node = TreeNode(int(data[i]))
            node.left, nextIndex = dfs(i+1)
            node.right, nextIndex = dfs(nextIndex)

            return [node, nextIndex]
        res, _ = dfs(0)

        return res