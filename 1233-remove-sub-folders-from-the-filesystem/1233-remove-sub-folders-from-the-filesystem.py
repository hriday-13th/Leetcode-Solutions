class Trie:
    def __init__(self, folder = ""):
        self.val = folder
        self.children = {}
        self.end = False
        
    def insert(self, s):
        node = self
        parts = s.split('/')
        for part in parts:
            if not part:
                continue
            if part not in node.children:
                node.children[part] = Trie(part)
            node = node.children[part]
        node.end = True
            
    def dfs(self, node = None, path = "", paths = None):
        if paths is None:
            paths = []
        if node is None:
            node = self
            
        if node.val:
            path += "/" + node.val
            
        if node.end:
            paths.append(path)
            return paths
        
        for child in node.children.values():
            self.dfs(child, path, paths)
            
        return paths
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        
        for f in folder:
            trie.insert(f)
            
        return trie.dfs()