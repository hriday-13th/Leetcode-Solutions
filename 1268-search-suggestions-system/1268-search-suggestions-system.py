class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = list()
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if node.n < 3:
                node.words.append(word)
                node.n += 1
                
    def search(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return ''
            node = node.children[c]
        return node.words
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)
            
        res = []
        pre = ''
        for c in searchWord:
            pre += c
            res.append(trie.search(pre))
            
        return res