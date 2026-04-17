class TreeNode:
    def __init__(self, isDir=True):
        self.children = {}
        self.isDir = isDir
        self.content = []

class Tree:
    def __init__(self):
        self.root = TreeNode()
    
    def mkdir(self, path):
        cur = self.root
        path = [p for p in path.split('/') if p]

        for p in path:
            if p not in cur.children:
                cur.children[p] = TreeNode()
            cur = cur.children[p]
    
    def addFile(self, file, content):
        cur = self.root
        path = [p for p in file.split('/') if p]

        for p in path:
            if p not in cur.children:
                cur.children[p] = TreeNode()
            cur = cur.children[p]

        cur.isDir = False
        cur.content.append(content)
    
    def readFile(self, file):
        cur = self.root
        path = [p for p in file.split('/') if p]

        for p in path:
            if p not in cur.children:
                cur.children[p] = TreeNode()
            cur = cur.children[p]
        
        return "".join(cur.content)
    
    def ls(self, path):
        cur = self.root
        path = [p for p in path.split('/') if p]

        for p in path:
            if p not in cur.children:
                cur.children[p] = TreeNode()
            cur = cur.children[p]
        
        if cur.isDir:
            return sorted(list(cur.children.keys()))
        else:
            return [path[-1]]

class FileSystem:

    def __init__(self):
        self.root = Tree()

    def ls(self, path: str) -> List[str]:
        return self.root.ls(path)

    def mkdir(self, path: str) -> None:
        self.root.mkdir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.root.addFile(filePath, content)

    def readContentFromFile(self, filePath: str) -> str:
        return self.root.readFile(filePath)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
