class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, node = None, index = 0):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
            
    def lookup(self, word, node = None, index = 0):
        if node is None:
            node = self.root
        if index == len(word):
            return node.is_end
        
        c = word[index]
        if c == ".":
            for child in node.children.values():
                if self.lookup(word, child, index + 1):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self.lookup(word, node.children[c], index + 1)
    
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.lookup(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)