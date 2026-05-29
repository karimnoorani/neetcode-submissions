class TreeNode:
    def __init__(self, val):
        self.children = {}
        self.val = val

class FileSystem:

    def __init__(self):
        self.files = TreeNode(0)

    def createPath(self, path: str, value: int) -> bool:
        pathList = path.split('/')[1:]
        cur = self.files

        for path in pathList[:-1]:
            if path not in cur.children:
                return False
            cur = cur.children[path]
        
        if pathList[-1] in cur.children:
            return False

        cur.children[pathList[-1]] = TreeNode(value)
        return True

    def get(self, path: str) -> int:
        pathList = path.split('/')[1:]
        cur = self.files

        for path in pathList:
            if path not in cur.children:
                return -1
            cur = cur.children[path]
        
        return cur.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
