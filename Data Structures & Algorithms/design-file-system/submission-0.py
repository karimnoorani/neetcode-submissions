class TreeNode:
    def __init__(self, val=0):
        self.children = {}
        self.val = val

class FileSystem:
    def __init__(self):
        self.root = TreeNode()

    def createPath(self, path: str, value: int) -> bool:
        cur = self.root
        f = path[1:].split('/')[-1]
        path = path[1:].split('/')[:-1] if path != "" and path != "/" else []

        for p in path:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        
        if f in cur.children:
            return False
        
        cur.children[f] = TreeNode(value)
        return True

    def get(self, path: str) -> int:
        cur = self.root
        path = path[1:].split('/') if path != "" and path != "/" else []

        for p in path:
            if p not in cur.children:
                return -1
            cur = cur.children[p]
        
        return cur.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
